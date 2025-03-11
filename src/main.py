from src.data_fetcher import DataFetcher
from src.db_manager import DatabaseManager
from src.parser import Parser

if __name__ == "__main__":
    DatabaseManager()

    steam_apps = DataFetcher().get_steam_apps()
    steam_apps_parsed = Parser().parse_steam_apps_data(steam_apps)

    DatabaseManager().insert_into_app_table(steam_apps_parsed)
