from typing import Optional
import sqlite3
from dtypes import SteamApp


class DatabaseManager:
    _instance: Optional["DatabaseManager"] = None

    def __new__(cls) -> "DatabaseManager":
        if cls._instance is None:
            cls._instance = super(DatabaseManager, cls).__new__(cls)
            cls._instance._initialize()
        return cls._instance

    def _initialize(self) -> None:
        self._connection = sqlite3.connect("steam.db")
        self._cursor = self._connection.cursor()

        # self._create_steam_apps_table()

    def _create_app_table(self) -> None:
        self._cursor.execute("CREATE TABLE app(app_id, name)")

    def insert_into_app_table(self, data: list[SteamApp]) -> None:
        self._cursor.executemany("INSERT INTO app VALUES(?, ?)", ((app.app_id, app.name) for app in data))
        self._connection.commit()
