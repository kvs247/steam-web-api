import json

from src.dtypes import SteamApp


class Parser:
    def __init__(self):
        pass

    def parse_steam_apps_data(self, steam_apps_str: str) -> list[SteamApp]:
        steam_apps_json = json.loads(steam_apps_str)
        steam_apps_list = steam_apps_json["applist"]["apps"]

        result: list[SteamApp] = []
        for app_item in steam_apps_list:
            steam_app = SteamApp(
                app_id=app_item["appid"],
                name=app_item["name"]
            )
            result.append(steam_app)

        return result
