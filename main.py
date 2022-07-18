import os

import emoji
import googlemaps
import tweepy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from weather_name.models import User
from owm import OWM, Weather, WEATHER_EMOJI


CONSUMER_KEY = os.getenv("CONSUMER_KEY")
CONSUMER_SECRET = os.getenv("CONSUMER_SECRET")

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
WEATHER_TOKEN = os.getenv("WEATHER_TOKEN")

engine = create_engine(os.getenv("DATABASE_URL"))


def get_weather_emoji(text):
    text = emoji.demojize(text)
    emoji_list = WEATHER_EMOJI.values()
    for e in emoji_list:
        if e in text:
            return e
    return


def get_location_point(address):
    gmaps = googlemaps.Client(key=GOOGLE_API_KEY)
    geocode_result = gmaps.geocode(address)
    if not geocode_result:
        return
    geocode_result, *_ = geocode_result
    location = geocode_result["geometry"]["location"]
    return location["lat"], location["lng"]


def replace_weather_name(db_user, user):
    name = emoji.demojize(user.name)
    target = get_weather_emoji(name)
    if not target:
        # 名前に絵文字がない場合
        return
    if not user.location:
        # 地名が登録されていない場合
        return
    point = None
    if db_user.location == user.location:
        lat, lon = (db_user.latitude, db_user.longitude)
        if lat and lon:
            point = (lat, lon)
    else:
        point = get_location_point(user.location)
    if not point:
        # 座標が取得できなかった場合
        return

    if db_user.location != user.location:
        db_user.location = user.location
        db_user.latitude, db_user.longitude = point
    w = OWM(WEATHER_TOKEN)
    response = w.get_weather_by_location(*point)
    json = response.json()
    weather = Weather.from_dict(json)
    name = name.replace(target, weather.get_emoji())
    return name


def run():
    Session = sessionmaker(engine)
    session = Session()
    users = session.query(User).all()
    for db_user in users:
        try:
            auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
            auth.set_access_token(db_user.access_token, db_user.access_token_secret)
            api = tweepy.API(auth)
            twitter_user = api.me()
            name = replace_weather_name(db_user, twitter_user)
            if name:
                api.update_profile(name=name)
        except tweepy.errors.TweepyException:
            session.delete(db_user)
    session.commit()


if __name__ == "__main__":
    run()
