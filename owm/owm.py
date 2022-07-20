from typing import Any, Dict

import requests


class OWM:
    DEFAULT_DATA_ENDPOINT = "https://openweathermap.org"
    DEFAULT_API_ENDPOINT = "https://api.openweathermap.org"

    def __init__(
        self,
        token: str,
        endpoint: str = DEFAULT_API_ENDPOINT,
        data_endpoint: str = DEFAULT_DATA_ENDPOINT,
    ) -> None:
        self.__token = token
        self.endpoint = endpoint
        self.data_endpoint = data_endpoint
        self.params = {"appid": self.__token}

    def _get(
        self,
        path: str,
        endpoint: str = None,
        params: Dict = None,
        stream: bool = False,
    ) -> requests.Response:
        url = (endpoint or self.endpoint) + path
        response = requests.get(url, params=params, stream=stream)
        return response

    def get_weather_by_city_name(
        self, city_name: str, mode: Any = None, units: Any = None, lang: Any = None
    ) -> requests.Response:
        params = {"q": city_name}
        params.update(self.params)
        response = self._get("/data/2.5/weather", params=params)
        return response

    def get_weather_by_location(
        self,
        lat: float,
        lon: float,
        mode: Any = None,
        units: Any = None,
        lang: Any = None,
    ) -> requests.Response:
        params = {"lat": lat, "lon": lon}
        params.update(self.params)
        response = self._get("/data/2.5/weather", params=params)
        return response

    def get_icon(self, icon_id: str) -> requests.Response:
        response = self._get(
            f"/img/wn/{icon_id}@2x.png", endpoint=self.data_endpoint, stream=True
        )
        return response
