import requests
from typing import Any, Optional
from nyxfall.card import Card
from nyxfall.paged_response import PagedResponse

SCRYFALL_BASE = "https://api.scryfall.com/cards/"
HEADERS = {"User-Agent": "NyxfallApp/0.0.1", "Accept": "*/*"}


def search_exact(name: str) -> Optional[Card]:
    req = requests.get(f"{SCRYFALL_BASE}named?exact={name}", headers=HEADERS)
    if req.status_code != requests.codes.ok:
        return None
    return _map_response(req.json())


def search_random() -> Card:
    return _map_response(requests.get(f"{SCRYFALL_BASE}random", headers=HEADERS).json())


def search_query(query: str, page_uri: Optional[str] = None) -> PagedResponse:
    uri = f"{SCRYFALL_BASE}search?q={query}&page=1" if page_uri is None else page_uri
    response = requests.get(uri, headers=HEADERS).json()
    return PagedResponse(
        next_page_uri=response.get("page", None),
        total_cards=response.get("total_cards", 0),
        has_more=response.get("has_more", False),
        data=[_map_response(card) for card in response["data"]],
    )


def _map_response(response: dict[str, Any]) -> Card:
    return Card(
        name=response.get("name", ""),
        scryfall_uri=response.get("scryfall_uri", ""),
        mana_cost=response.get("mana_cost", ""),
        type_line=response.get("type_line", ""),
        power=response.get("power", None),
        toughness=response.get("toughness", None),
        oracle_text=response.get("oracle_text", ""),
        flavor_text=response.get("flavor_text", None),
        set=response.get("set", "").upper(),
    )
