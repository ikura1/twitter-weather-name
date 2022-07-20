from typing import Dict

import emoji
from typing_extensions import Self

WEATHER_EMOJI = {
    "01": ":sun:",
    "02": ":sun_behind_cloud:",
    "10": ":sun_behind_rain_cloud:",
    "03": ":cloud:",
    "04": ":cloud:",
    "09": ":cloud_with_rain:",
    "11": ":cloud_with_lightning:",
    "13": ":snowman:",
    "50": ":fog:",
}


class Weather:
    def __init__(self, code: int, main: str, description: str, icon: str) -> None:
        """
        [
            {
                'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02d'
            }
        ],
        """
        self.code = code
        self.main = main
        self.description = description
        self.icon = icon

    def get_icon_url(self) -> str:
        return

    def get_emoji(self) -> str:
        return emoji.emojize(WEATHER_EMOJI[self.icon[:-1]])

    @classmethod
    def from_dict(cls, dict_: Dict) -> Self:
        weather, *_ = dict_.get("weather", {})
        return Weather(
            weather.get("id"),
            weather.get("main"),
            weather.get("description"),
            weather.get("icon"),
        )
