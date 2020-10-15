import os

import emoji
import googlemaps
import tweepy

from owm import OWM
from weather import Weather, WEATHER_EMOJI

CONSUMER_KEY = os.getenv("CONSUMER_KEY")
CONSUMER_SECRET = os.getenv("CONSUMER_SECRET")
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
ACCESS_TOKEN_SECRET = os.getenv("ACCESS_TOKEN_SECRET")

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
WEATHER_TOKEN = os.getenv("WEATHER_TOKEN")


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


def run():
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth)
    user = api.me()
    name = emoji.demojize(user.name)
    target = get_weather_emoji(name)
    if not target:
        return

    point = get_location_point(user.location)
    if not point:
        return

    w = OWM(WEATHER_TOKEN)
    response = w.get_weather_by_location(*point)
    json = response.json()
    weather = Weather.from_dict(json)
    name = name.replace(target, weather.get_emoji())
    api.update_profile(name=name)


if __name__ == "__main__":
    run()