import os
from weather import Weather, WEATHER_EMOJI

import emoji
import tweepy

from owm import OWM

CONSUMER_KEY = os.getenv("CONSUMER_KEY")
CONSUMER_SECRET = os.getenv("CONSUMER_SECRET")
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
ACCESS_TOKEN_SECRET = os.getenv("ACCESS_TOKEN_SECRET")

WEATHER_TOKEN = os.getenv("WEATHER_TOKEN")


def get_weather_emoji(text):
    text = emoji.demojize(text)
    emoji_list = WEATHER_EMOJI.values()
    for e in emoji_list:
        if e in text:
            return e
    return


def run():
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth)

    w = OWM(WEATHER_TOKEN)
    response = w.get_weather_by_city_name("Osaka")
    json = response.json()
    weather = Weather.from_dict(json)
    user = api.me()
    name = emoji.demojize(user.name)
    target = get_weather_emoji(name)
    if not target:
        return
    name = name.replace(target, weather.get_emoji())
    api.update_profile(name=name)


if __name__ == "__main__":
    run()