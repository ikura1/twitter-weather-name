import unittest

import emoji

from owm import Weather

WEATHER_DICT = {
    "weather": [
        {"id": 801, "main": "Clouds", "description": "few clouds", "icon": "02d"}
    ]
}


class TestWeather(unittest.TestCase):
    def test_weather(self):
        weather = Weather.from_dict(WEATHER_DICT)
        self.assertIsInstance(weather, Weather)

    def test_weather_emoji(self):
        weather = Weather.from_dict(WEATHER_DICT)
        e = weather.get_emoji()
        self.assertEqual(e, emoji.emojize(":sun_behind_cloud:"))


if __name__ == "__main__":
    unittest.main()
