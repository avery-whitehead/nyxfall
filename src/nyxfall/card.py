from dataclasses import dataclass
from typing import Optional
from textwrap import fill

CARD_TEXT_DEFAULT_WIDTH = 32
# When rendering a card, leave a reasonable space between the end of the name and the start of the mana cost
NAME_MANA_COST_GAP = 2


@dataclass
class Card:
    """Data required to display an MTG card

    Attributes:
        name: Colossal Dreadmaw
        scryfall_uri: https://scryfall.com/card/m21/176/colossal-dreadmaw
        mana_cost: {4}{G}{G}
        type_line: Creature — Dinosaur
        power: 6
        toughness: 6
        oracle_text: Trample (This creature can deal excess combat damage to the player or planeswalker it's attacking.)
        flavor_text: If you feel the ground quake, run. If you hear its bellow, flee. If you see its teeth, it's too late.
        set: XLN
        collector_number: 180
        rarity: C
    """

    name: str
    scryfall_uri: str
    mana_cost: str
    type_line: str
    power: Optional[str]
    toughness: Optional[str]
    oracle_text: str
    flavor_text: Optional[str]
    set: str

    def print_as_card(self) -> None:
        """Formats a ``Card`` in a card-looking way and prints it out"""
        # Defalt card width to 30 characters unless the card has a particularly long name or mana cost
        card_text_width = (
            CARD_TEXT_DEFAULT_WIDTH
            if max(
                (len(self.name) + len(self.mana_cost) + NAME_MANA_COST_GAP),
                len(self.type_line),
            )
            <= CARD_TEXT_DEFAULT_WIDTH
            else max(
                (len(self.name) + len(self.mana_cost) + NAME_MANA_COST_GAP),
                len(self.type_line),
            )
        )

        # Initialise a string list with everything up until the first conditonal section
        # of the display. It will be appended to later and joined with a newline separator at the end
        card = [
            # Top of outside bounding box
            f"┌{"─" * (card_text_width + 2)}┐",
            # Name and mana cost
            f"│┌{"─" * card_text_width}┐│",
            f"││{self.name}{" " * (card_text_width - len(self.name) - len(self.mana_cost))}{self.mana_cost}││",
            f"│└┬{"─" * (card_text_width - 2)}┬┘│",
            # Empty image box
            "\n".join([f"│ │{" " * (card_text_width - 2)}│ │"] * 7),
            # Type line
            f"│┌┴{"─" * (card_text_width - 2)}┴┐│",
            f"││{self.type_line}{" " * (card_text_width - len(self.type_line))}││",
            f"│└┬{"─" * (card_text_width - 2)}┬┘│",
            # Oracle text
            self._wrap_and_pad(self.oracle_text, card_text_width),
        ]

        # Flavour text
        if self.flavor_text:
            card.append(f"│ │ {"─" * (card_text_width - 4)} │ │")
            # Append and prepend flavour text with ANSI escape code for italics
            card.append(
                "\x1B[3m"
                + self._wrap_and_pad(self.flavor_text, card_text_width)
                + "\x1B[23m"
            )

        if self.power and self.toughness:
            # Width of characters in power and toughness plus 3 for the forward slash and spacing
            pt_box_width = len(str(self.power)) + len(str(self.toughness)) + 3
            pt_box = [
                f"│ │{" " * (card_text_width - pt_box_width - 4)}┌{"─" * pt_box_width}┐│ │",
                f"│ └─{"─" * (card_text_width - pt_box_width - 5)}┤ {str(self.power)}/{str(self.toughness)} ├┘ │",
                f"│ {self.set}{" " * (card_text_width - len(self.set) - pt_box_width - 3)}└─────┘  │",
                f"└{"─" * (card_text_width + 2)}┘",
            ]
            card.extend(pt_box)
        else:
            set_box = [
                f"│ └{"─" * (card_text_width - 2)}┘ │",
                f"│ {self.set}{" " * (card_text_width - len(self.set))} │",
                f"└{"─" * (card_text_width + 2)}┘",
            ]
            card.extend(set_box)
        print("\n".join(card) + "\n")

    def _wrap_and_pad(self, text: str, card_width: int) -> str:
        """Helper function that breaks long strings on to newlines and pads each line

        Args:
            text: Text to be wrapped and padded (e.g. oracle text, flavour text)
            card_width: Width of the card (naturally the width text will be padded to)

        Returns:
            String of ``text`` with newline breaks and padded out to card width length
        """
        # Passing a string with newline characters to textwrap.fill() causes some ugly line
        # breaks, so we want to tell it to ignore linebreaks. This will create a list of strings
        # where each element is where we want to break, but each element will also include
        # the original newlines, so we need to split again on those newlines, flatten those
        # sub-lists and then finally return that list joined with newline as a separator
        return "\n".join(
            [
                f"│ │{line}{" " * (card_width - len(line) - 2)}│ │"
                for lines in [
                    fill(
                        paragraph,
                        width=card_width - 2,
                        replace_whitespace=False,
                    ).split("\n")
                    for paragraph in text.splitlines()
                ]
                for line in lines
            ]
        )
