from dataclasses import dataclass
from typing import Optional
from textwrap import fill

CARD_DEFAULT_WIDTH = 32
# When rendering a card, leave a reasonable space between the end of the name and the start of the mana cost
NAME_MANA_COST_GAP: int = 2


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
    """

    name: str
    scryfall_uri: str
    mana_cost: Optional[str]
    type_line: str
    power: Optional[str]
    toughness: Optional[str]
    oracle_text: str
    flavor_text: Optional[str]
    set: str

    def print_as_card(self) -> None:
        """Formats a ``Card`` in a card-looking way and prints it out"""
        # Defalt card width to 30 characters unless the card has a particularly long name or mana cost
        card_width = (
            CARD_DEFAULT_WIDTH
            if (len(self.name) + len(self.mana_cost) + NAME_MANA_COST_GAP)
            <= CARD_DEFAULT_WIDTH
            else len(self.name) + len(self.mana_cost) + NAME_MANA_COST_GAP
        )

        # Initialise a string list with everything up until the first conditonal section
        # of the display. It will be appended to later and joined with a newline separator at the end
        card = [
            # Name and mana cost
            f"+{"-" * card_width}+",
            f"|{self.name}{" " * (card_width - len(self.name) - len(self.mana_cost))}{self.mana_cost}|",
            f"+{"-" * card_width}+",
            # (empty) image box
            "\n".join([f"|{" " * card_width}|"] * 3),
            f"+{"-" * card_width}+",
        ]

        # Type line
        if len(self.type_line) < card_width:
            card.append(f"|{self.type_line}{" " * (card_width - len(self.type_line))}|")
        else:
            card.append(self._wrap_and_pad(self.type_line, card_width))
        card.append(f"+{"-" * card_width}+")

        # Oracle text
        card.append(self._wrap_and_pad(self.oracle_text, card_width))

        # Flavour text
        if self.flavor_text:
            card.append(f"|  {"-" * (card_width - 4)}  |")
            # Append and prepend flavour text with ANSI escape code for italics
            card.append(
                "\x1B[3m"
                + self._wrap_and_pad(self.flavor_text, card_width)
                + "\x1B[23m"
            )

        if self.power and self.toughness:
            # Width of characters in power and toughness plus 3 for the forward slash and spacing
            pt_box_width = len(str(self.power)) + len(str(self.toughness)) + 3
            pt_box = [
                f"|{" " * (card_width - pt_box_width - 1)}+{"-" * pt_box_width}+",
                f"|{" " * (card_width - pt_box_width - 1)}| {str(self.power)}/{str(self.toughness)} |",
                f"+{"-" * (card_width - pt_box_width - 1)}+{"-" * pt_box_width}+",
            ]
            card.extend(pt_box)
        else:
            card.append(f"+{"-" * card_width}+")
        print("\n".join(card))

    def _wrap_and_pad(self, text: str, card_width: int) -> str:
        """Helper function that breaks long strings on to newlines and pads each line

        Args:
            text: Text to be wrapped and padded (e.g. type lines, oracle text)
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
                f"|{line}{" " * (card_width - len(line))}|"
                for lines in [
                    fill(
                        paragraph,
                        width=CARD_DEFAULT_WIDTH,
                        replace_whitespace=False,
                    ).split("\n")
                    for paragraph in text.splitlines()
                ]
                for line in lines
            ]
        )
