import requests


class DataFetcher:
    def __init__(self):
        pass

    def get_steam_apps(self) -> str:
        url = "https://api.steampowered.com/ISteamApps/GetAppList/v2/"
        r = requests.get(url)

        if r.status_code != 200:
            print(f"error getting steam apps data: {r.text} ({r.status_code})")
            return ""
        else:
            return r.text
