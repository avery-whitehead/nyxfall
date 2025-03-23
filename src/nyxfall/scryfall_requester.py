import time
import requests
from typing import Any, Optional
from nyxfall.card import Card
from nyxfall.card_face import CardFace

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
    return _map_response(
        requests.get(f"{SCRYFALL_BASE}random", headers=HEADERS).json()
    )


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
    if response.get("card_faces") is None:
        return Card(
            faces=[_map_card_face(response)], name=response.get("name", "")
        )

    return Card(
        faces=[
            _map_card_face(face) for face in response.get("card_faces", [])
        ],
        name=response.get("name", ""),
    )


def _map_card_face(face: dict[str, Any]) -> CardFace:
    return CardFace(
        name=face.get("name", ""),
        scryfall_uri=face.get("scryfall_uri", ""),
        mana_cost=face.get("mana_cost", ""),
        type_line=face.get("type_line", ""),
        power=face.get("power", None),
        toughness=face.get("toughness", None),
        oracle_text=face.get("oracle_text", ""),
        flavor_text=face.get("flavor_text", None),
        set=face.get("set", "").upper(),
    )
