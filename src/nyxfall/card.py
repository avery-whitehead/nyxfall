from dataclasses import dataclass
from nyxfall.card_face import CardFace


@dataclass
class Card:
    """A card with one or more faces to be displayed"""

    faces: list[CardFace]
    name: str
