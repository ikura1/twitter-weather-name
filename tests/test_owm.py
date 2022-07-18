import os
import unittest

from owm import OWM

WEATHER_TOKEN = os.getenv("WEATHER_TOKEN")


class TestOWM(unittest.TestCase):
    def setUp(self):
        self.w = OWM(WEATHER_TOKEN)

    def test_owm(self):
        w = OWM(WEATHER_TOKEN)
        self.assertIsInstance(w, OWM)

    def test_weather_by_city(self):
        correct = {
            "coord": {"lon": 139.6917, "lat": 35.6895},
            "base": "stations",
            "timezone": 32400,
            "id": 1850144,
            "name": "Tokyo",
            "cod": 200,
        }
        city = "Tokyo"
        res = self.w.get_weather_by_city_name(city)
        # 200のチェック
        self.assertEqual(200, res.status_code)
        res_json = res.json()
        # 形のチェック
        self.assertLessEqual(correct.items(), res_json.items())
        # 天気が存在するか
        self.assertIn("weather", res_json)

    def test_weather_by_location(self):
        correct = {
            "coord": {"lon": 139.6503, "lat": 35.6762},
            "base": "stations",
            "timezone": 32400,
            "id": 1862143,
            "name": "Horinouchi",
            "cod": 200,
        }
        lat, lon = 35.6761919, 139.6503106
        res = self.w.get_weather_by_location(lat, lon)
        self.assertEqual(200, res.status_code)
        res_json = res.json()
        # 形のチェック
        self.assertLessEqual(correct.items(), res_json.items())
        # 天気が存在するか
        self.assertIn("weather", res_json)
