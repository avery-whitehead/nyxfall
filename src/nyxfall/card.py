from dataclasses import dataclass
from typing import Optional


@dataclass
class Card:
    name: str
    scryfall_uri: str
    cmc: float
    mana_cost: Optional[str]
    colors: list[str]
    type_line: str
    power: Optional[str]
    toughness: Optional[str]
    oracle_text: str
    set: str
