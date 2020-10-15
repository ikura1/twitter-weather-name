import emoji


class Weather:
    def __init__(self, code, main, description, icon):
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

    def get_icon_url(self):
        return

    def get_emoji(self):
        emoji_dict = {
            "01d": ":sun:",
            "02d": ":sun_behind_cloud:",
            "10d": ":sun_behind_rain_cloud:",
            "03d": ":cloud:",
            "04d": ":cloud:",
            "09d": ":cloud_with_rain:",
            "11d": ":cloud_with_lightning:",
            "13d": ":snowman:",
            "50d": ":fog:",
        }
        return emoji.emojize(emoji_dict[self.icon])

    @classmethod
    def from_dict(cls, dict_):
        weather, *_ = dict_.get("weather", {})
        return Weather(
            weather.get("id"),
            weather.get("main"),
            weather.get("description"),
            weather.get("icon"),
        )
