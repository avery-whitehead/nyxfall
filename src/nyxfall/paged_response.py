from dataclasses import dataclass
from typing import Optional
from nyxfall.card import Card


@dataclass
class PagedResponse:
    """A paged response from a Scryfall query containing multiple cards

    Attributes:
        page: Page of the response, starts at 1
        total_cards: Number of cards that match the query
        has_more: True if there are more pages, false if this is the last page
        data: ``Card`` objects returned in this page
    """

    next_page_uri: Optional[str]
    total_cards: int
    has_more: bool
    data: list[Card]
