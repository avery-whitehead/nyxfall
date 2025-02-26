from dataclasses import dataclass
from typing import Optional


@dataclass
class Card:
    scryfall_uri: str
    cmc: float
    mana_cost: str
    colors: list[str]
    type_line: str
    power: Optional[str]
    toughness: Optional[str]
    oracle_text: str
    set: str
