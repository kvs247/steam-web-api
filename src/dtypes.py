from dataclasses import dataclass


@dataclass
class SteamApp:
    app_id: int
    name: str
