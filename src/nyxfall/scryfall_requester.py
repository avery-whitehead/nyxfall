import time
import requests
from typing import Any, Optional
from nyxfall.card import Card

SCRYFALL_BASE = "https://api.scryfall.com/cards/"
HEADERS = {"User-Agent": "NyxfallApp/0.0.1", "Accept": "*/*"}


def search_exact(name: str) -> Optional[Card]:
    """Searches for a card with the name exactly matching a string

    Args:
        name: Name of card to match

    Returns:
        ``Card`` object matching that string if one was found, None otherwise
    """
    req = requests.get(f"{SCRYFALL_BASE}named?exact={name}", headers=HEADERS)
    if req.status_code != requests.codes.ok:
        return None
    return _map_response(req.json())


def search_random() -> Card:
    """Searches for a random card

    Returns:
        ``Card`` object of a random card
    """
    return _map_response(requests.get(f"{SCRYFALL_BASE}random", headers=HEADERS).json())


def search_query(query: str) -> list[Card]:
    """Searches for a query and returns all cards that match

    Args:
        query: Query to execute

    Returns:
        All ``Card`` objects matching the query, or an empty list of no cards were found
    """
    response = requests.get(
        f"{SCRYFALL_BASE}search?q={query}+game:paper&page=1", headers=HEADERS
    ).json()
    card_data = [_map_response(card) for card in response.get("data", [])]

    # Traverse pagination from responses
    while response.get("has_more", False):
        # Rate limit ourselves by 100ms between requests
        time.sleep(100 / 1000)
        response = requests.get(response.get("next_page", "")).json()
        card_data += [_map_response(card) for card in response.get("data", [])]

    return card_data


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
