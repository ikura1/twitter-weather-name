import requests


class OWM:
    DEFAULT_DATA_ENDPOINT = "https://openweathermap.org"
    DEFAULT_API_ENDPOINT = "https://api.openweathermap.org"

    def __init__(
        self, token, endpoint=DEFAULT_API_ENDPOINT, data_endpoint=DEFAULT_DATA_ENDPOINT
    ):
        self.__token = token
        self.endpoint = endpoint
        self.data_endpoint = data_endpoint
        self.params = {"appid": self.__token}

    def _get(
        self,
        path,
        endpoint=None,
        params=None,
        stream=False,
    ):
        url = (endpoint or self.endpoint) + path
        response = requests.get(url, params=params, stream=stream)
        return response

    def get_weather_by_city_name(self, city_name, mode=None, units=None, lang=None):
        params = {"q": city_name}
        params.update(self.params)
        response = self._get("/data/2.5/weather", params=params)
        return response

    def get_weather_by_location(self, lat, lon, mode=None, units=None, lang=None):
        params = {"lat": lat, "lon": lon}
        params.update(self.params)
        response = self._get("/data/2.5/weather", params=params)
        return response

    def get_icon(self, icon_id):
        response = self._get(
            f"/img/wn/{icon_id}@2x.png", endpoint=self.data_endpoint, stream=True
        )
        return response
