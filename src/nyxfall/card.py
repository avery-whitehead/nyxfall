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

    def format_as_card(self, ascii_only: bool = False) -> str:
        """Builds a string that will display a ``Card`` similar to an actual MTG card

        Args:
            ascii_only: True if card frame should be rendered using only the basic ASCII set

        Returns:
            Formatted and newline-separated string that should display a card when printed
        """
        down_right = "+" if ascii_only else "┌"
        down_left = "+" if ascii_only else "┐"
        up_right = "+" if ascii_only else "└"
        up_left = "+" if ascii_only else "┘"
        vertical = "|" if ascii_only else "│"
        horizontal = "-" if ascii_only else "─"
        down_horizontal = "+" if ascii_only else "┬"
        up_horizontal = "+" if ascii_only else "┴"
        left_vertical = "|" if ascii_only else "┤"
        right_vertical = "|" if ascii_only else "├"

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
            f"{down_right}{horizontal * (card_text_width + 2)}{down_left}",
            # Name and mana cost
            f"{vertical}{down_right}{horizontal * card_text_width}{down_left}{vertical}",
            f"{vertical}{vertical}{self.name}{" " * (card_text_width - len(self.name) - len(self.mana_cost))}{self.mana_cost}{vertical}{vertical}",
            f"{vertical}{up_right}{down_horizontal}{horizontal * (card_text_width - 2)}{down_horizontal}{up_left}{vertical}",
            # Empty image box
            "\n".join(
                [
                    f"{vertical} {vertical}{" " * (card_text_width - 2)}{vertical} {vertical}"
                ]
                * 1
            ),
            # Type line
            f"{vertical}{down_right}{up_horizontal}{horizontal * (card_text_width - 2)}{up_horizontal}{down_left}{vertical}",
            f"{vertical}{vertical}{self.type_line}{" " * (card_text_width - len(self.type_line))}{vertical}{vertical}",
            f"{vertical}{up_right}{down_horizontal}{horizontal * (card_text_width - 2)}{down_horizontal}{up_left}{vertical}",
            # Oracle text
            self._wrap_and_pad(self.oracle_text, card_text_width, vertical),
        ]

        # Flavour text
        if self.flavor_text:
            card.append(
                f"{vertical} {vertical} {horizontal * (card_text_width - 4)} {vertical} {vertical}"
            )
            # Append and prepend flavour text with ANSI escape code for italics
            card.append(
                ("" if ascii_only else "\x1B[3m")
                + self._wrap_and_pad(self.flavor_text, card_text_width, vertical)
                + ("" if ascii_only else "\x1B[23m")
            )

        if self.power and self.toughness:
            # Width of characters in power and toughness plus 3 for the forward slash and spacing
            pt_box_width = len(str(self.power)) + len(str(self.toughness)) + 3
            pt_box = [
                f"{vertical} {vertical}{" " * (card_text_width - pt_box_width - 4)}{down_right}{horizontal * pt_box_width}{down_left}{vertical} {vertical}",
                f"{vertical} {up_right}{horizontal * (card_text_width - pt_box_width - 4)}{left_vertical} {str(self.power)}/{str(self.toughness)} {right_vertical}{up_left} {vertical}",
                f"{vertical} {self.set}{" " * (card_text_width - len(self.set) - pt_box_width - 3)}{up_right}{horizontal * 5}{up_left}  {vertical}",
                f"{up_right}{horizontal * (card_text_width + 2)}{up_left}",
            ]
            card.extend(pt_box)
        else:
            set_box = [
                f"{vertical} {up_right}{horizontal * (card_text_width - 2)}{up_left} {vertical}",
                f"{vertical} {self.set}{" " * (card_text_width - len(self.set))} {vertical}",
                f"{up_right}{horizontal * (card_text_width + 2)}{up_left}",
            ]
            card.extend(set_box)

        return "\n".join(card) + "\n"

    def _wrap_and_pad(self, text: str, card_width: int, vert_char: str) -> str:
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
                f"{vert_char} {vert_char}{line}{" " * (card_width - len(line) - 2)}{vert_char} {vert_char}"
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
