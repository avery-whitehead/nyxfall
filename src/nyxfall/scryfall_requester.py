import requests
from typing import Optional
from nyxfall.card import Card

SCRYFALL_BASE = "https://api.scryfall.com/cards/"


def search_exact(name: str) -> Optional[Card]:
    req = requests.get(f"{SCRYFALL_BASE}named?exact={name}")
    if req.status_code != requests.codes.ok:
        return None
    return map_response(req.json())


def search_random() -> Card:
    return map_response(requests.get(f"{SCRYFALL_BASE}random").json())


def map_response(response: dict[str, any]) -> Card:
    return Card(
        name=response.get("name", ""),
        scryfall_uri=response.get("scryfall_uri", ""),
        cmc=response.get("cmc", ""),
        mana_cost=response.get("mana_cost", None),
        colors=response.get("colors", []),
        type_line=response.get("type_line", ""),
        power=response.get("power", None),
        toughness=response.get("toughness", None),
        oracle_text=response.get("oracle_text", ""),
        set=response.get("set", "").upper(),
    )
