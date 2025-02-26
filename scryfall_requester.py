import requests
from typing import Optional
from card import Card

SCRYFALL_BASE = "https://api.scryfall.com/cards/"


def search_exact(name: str) -> Optional[Card]:
    req = requests.get(f"{SCRYFALL_BASE}named?exact={name}")
    if req.status_code != requests.codes.ok:
        return None
    return map_response(req.json())


def search_random() -> Card:
    return map_response(requests.get(f"{SCRYFALL_BASE}random").json())


def map_response(response: dict) -> Card:
    return Card(
        scryfall_uri=response["scryfall_uri"],
        cmc=response["cmc"],
        mana_cost=response["mana_cost"],
        colors=response["colors"],
        type_line=response["type_line"],
        power=response.get("power", None),
        toughness=response.get("toughness", None),
        oracle_text=response["oracle_text"],
        set=response["set"].upper(),
    )
