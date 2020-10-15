import os
from weather import Weather

import tweepy

from owm import OWM

CONSUMER_KEY = os.getenv("CONSUMER_KEY")
CONSUMER_SECRET = os.getenv("CONSUMER_SECRET")
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
ACCESS_TOKEN_SECRET = os.getenv("ACCESS_TOKEN_SECRET")

WEATHER_TOKEN = os.getenv("WEATHER_TOKEN")


def run():
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth)

    w = OWM(WEATHER_TOKEN)
    response = w.get_weather_by_city_name("Osaka")
    json = response.json()
    weather = Weather.from_dict(json)

    api.update_profile(name=f"イクラ{weather.get_emoji()}")


if __name__ == "__main__":
    run()