from nyxfall.card import Card


def test_extended_ascii_no_pt():
    expected_str = (
        "\n".join(
            [
                "┌──────────────────────────────────┐",
                "│┌────────────────────────────────┐│",
                "││Lightning Bolt               {R}││",
                "│└┬──────────────────────────────┬┘│",
                "│ │                              │ │",
                "│┌┴──────────────────────────────┴┐│",
                "││Instant                         ││",
                "│└┬──────────────────────────────┬┘│",
                "│ │Lightning Bolt deals 3 damage │ │",
                "│ │to any target.                │ │",
                "│ │ ──────────────────────────── │ │",
                "\x1b[3m│ │The sparkmage shrieked,       │ │",
                "│ │calling on the rage of the    │ │",
                "│ │storms of his youth. To his   │ │",
                "│ │surprise, the sky responded   │ │",
                "│ │with a fierce energy he'd     │ │",
                "│ │never thought to see again.   │ │\x1b[23m",
                "│ └──────────────────────────────┘ │",
                "│ CLU                              │",
                "└──────────────────────────────────┘",
            ]
        )
        + "\n"
    )
    card = Card(
        name="Lightning Bolt",
        scryfall_uri="",
        mana_cost="{R}",
        type_line="Instant",
        power=None,
        toughness=None,
        oracle_text="Lightning Bolt deals 3 damage to any target.",
        flavor_text="The sparkmage shrieked, calling on the rage of the storms of his youth. To his surprise, the sky responded with a fierce energy he'd never thought to see again.",
        set="CLU",
    )

    assert card.format_as_card() == expected_str


def test_extended_ascii_pt():
    expected_str = (
        "\n".join(
            [
                "┌──────────────────────────────────┐",
                "│┌────────────────────────────────┐│",
                "││Colossal Dreadmaw      {4}{G}{G}││",
                "│└┬──────────────────────────────┬┘│",
                "│ │                              │ │",
                "│┌┴──────────────────────────────┴┐│",
                "││Creature — Dinosaur             ││",
                "│└┬──────────────────────────────┬┘│",
                "│ │Trample (This creature can    │ │",
                "│ │deal excess combat damage to  │ │",
                "│ │the player or planeswalker    │ │",
                "│ │it's attacking.)              │ │",
                "│ │ ──────────────────────────── │ │",
                "\x1b[3m│ │If you feel the ground quake, │ │",
                "│ │run. If you hear its bellow,  │ │",
                "│ │flee. If you see its teeth,   │ │",
                "│ │it's too late.                │ │\x1b[23m",
                "│ │                       ┌─────┐│ │",
                "│ └───────────────────────┤ 6/6 ├┘ │",
                "│ M21                     └─────┘  │",
                "└──────────────────────────────────┘",
            ]
        )
        + "\n"
    )
    card = Card(
        name="Colossal Dreadmaw",
        scryfall_uri="",
        mana_cost="{4}{G}{G}",
        type_line="Creature — Dinosaur",
        power="6",
        toughness="6",
        oracle_text="Trample (This creature can deal excess combat damage to the player or planeswalker it's attacking.)",
        flavor_text="If you feel the ground quake, run. If you hear its bellow, flee. If you see its teeth, it's too late.",
        set="M21",
    )

    assert card.format_as_card() == expected_str


def test_basic_ascii_no_pt():
    expected_str = (
        "\n".join(
            [
                "+----------------------------------+",
                "|+--------------------------------+|",
                "||Lightning Bolt               {R}||",
                "|++------------------------------++|",
                "| |                              | |",
                "|++------------------------------++|",
                "||Instant                         ||",
                "|++------------------------------++|",
                "| |Lightning Bolt deals 3 damage | |",
                "| |to any target.                | |",
                "| | ---------------------------- | |",
                "| |The sparkmage shrieked,       | |",
                "| |calling on the rage of the    | |",
                "| |storms of his youth. To his   | |",
                "| |surprise, the sky responded   | |",
                "| |with a fierce energy he'd     | |",
                "| |never thought to see again.   | |",
                "| +------------------------------+ |",
                "| CLU                              |",
                "+----------------------------------+",
            ]
        )
        + "\n"
    )

    card = Card(
        name="Lightning Bolt",
        scryfall_uri="",
        mana_cost="{R}",
        type_line="Instant",
        power=None,
        toughness=None,
        oracle_text="Lightning Bolt deals 3 damage to any target.",
        flavor_text="The sparkmage shrieked, calling on the rage of the storms of his youth. To his surprise, the sky responded with a fierce energy he'd never thought to see again.",
        set="CLU",
    )

    assert card.format_as_card(ascii_only=True) == expected_str


def test_basic_ascii_pt():
    expected_str = (
        "\n".join(
            [
                "+----------------------------------+",
                "|+--------------------------------+|",
                "||Colossal Dreadmaw      {4}{G}{G}||",
                "|++------------------------------++|",
                "| |                              | |",
                "|++------------------------------++|",
                "||Creature — Dinosaur             ||",
                "|++------------------------------++|",
                "| |Trample (This creature can    | |",
                "| |deal excess combat damage to  | |",
                "| |the player or planeswalker    | |",
                "| |it's attacking.)              | |",
                "| | ---------------------------- | |",
                "| |If you feel the ground quake, | |",
                "| |run. If you hear its bellow,  | |",
                "| |flee. If you see its teeth,   | |",
                "| |it's too late.                | |",
                "| |                       +-----+| |",
                "| +-----------------------| 6/6 |+ |",
                "| M21                     +-----+  |",
                "+----------------------------------+",
            ]
        )
        + "\n"
    )

    card = Card(
        name="Colossal Dreadmaw",
        scryfall_uri="",
        mana_cost="{4}{G}{G}",
        type_line="Creature — Dinosaur",
        power="6",
        toughness="6",
        oracle_text="Trample (This creature can deal excess combat damage to the player or planeswalker it's attacking.)",
        flavor_text="If you feel the ground quake, run. If you hear its bellow, flee. If you see its teeth, it's too late.",
        set="M21",
    )

    assert card.format_as_card(ascii_only=True) == expected_str


def test_long_name_no_pt():
    expected_str = (
        "\n".join(
            [
                "┌──────────────────────────────────────┐",
                "│┌────────────────────────────────────┐│",
                "││Realmbreaker, the Invasion Tree  {3}││",
                "│└┬──────────────────────────────────┬┘│",
                "│ │                                  │ │",
                "│┌┴──────────────────────────────────┴┐│",
                "││Legendary Artifact                  ││",
                "│└┬──────────────────────────────────┬┘│",
                "│ │{2}, {T}: Target opponent mills   │ │",
                "│ │three cards. Put a land card from │ │",
                "│ │their graveyard onto the          │ │",
                "│ │battlefield tapped under your     │ │",
                '│ │control. It gains "If this land   │ │',
                "│ │would leave the battlefield, exile│ │",
                "│ │it instead of putting it anywhere │ │",
                '│ │else."                            │ │',
                "│ │{10}, {T}, Sacrifice Realmbreaker:│ │",
                "│ │Search your library for any number│ │",
                "│ │of Praetor cards, put them onto   │ │",
                "│ │the battlefield, then shuffle.    │ │",
                "│ └──────────────────────────────────┘ │",
                "│ MOM                                  │",
                "└──────────────────────────────────────┘",
            ]
        )
        + "\n"
    )

    card = Card(
        name="Realmbreaker, the Invasion Tree",
        scryfall_uri="",
        mana_cost="{3}",
        type_line="Legendary Artifact",
        power=None,
        toughness=None,
        oracle_text='{2}, {T}: Target opponent mills three cards. Put a land card from their graveyard onto the battlefield tapped under your control. It gains "If this land would leave the battlefield, exile it instead of putting it anywhere else."\n{10}, {T}, Sacrifice Realmbreaker: Search your library for any number of Praetor cards, put them onto the battlefield, then shuffle.',
        flavor_text=None,
        set="MOM",
    )

    assert card.format_as_card() == expected_str


def test_long_type_line_pt():
    expected_str = (
        "\n".join(
            [
                "┌───────────────────────────────────────────────────┐",
                "│┌─────────────────────────────────────────────────┐│",
                "││The Reality Chip                           {1}{U}││",
                "│└┬───────────────────────────────────────────────┬┘│",
                "│ │                                               │ │",
                "│┌┴───────────────────────────────────────────────┴┐│",
                "││Legendary Artifact Creature - Equipment Jellyfish││",
                "│└┬───────────────────────────────────────────────┬┘│",
                "│ │You may look at the top card of your library   │ │",
                "│ │any time.                                      │ │",
                "│ │As long as The Reality Chip is attached to a   │ │",
                "│ │creature, you may play lands and cast spells   │ │",
                "│ │from the top of your library.                  │ │",
                "│ │Reconfigure {2}{U} ({2}{U}: Attach to target   │ │",
                "│ │creature you control; or unattach from a       │ │",
                "│ │creature. Reconfigure only as a sorcery. While │ │",
                "│ │attached, this isn't a creature.)              │ │",
                "│ │                                        ┌─────┐│ │",
                "│ └────────────────────────────────────────┤ 0/4 ├┘ │",
                "│ NEO                                      └─────┘  │",
                "└───────────────────────────────────────────────────┘",
            ]
        )
        + "\n"
    )

    card = Card(
        name="The Reality Chip",
        scryfall_uri="",
        mana_cost="{1}{U}",
        type_line="Legendary Artifact Creature - Equipment Jellyfish",
        power="0",
        toughness="4",
        oracle_text="You may look at the top card of your library any time.\nAs long as The Reality Chip is attached to a creature, you may play lands and cast spells from the top of your library.\nReconfigure {2}{U} ({2}{U}: Attach to target creature you control; or unattach from a creature. Reconfigure only as a sorcery. While attached, this isn't a creature.)",
        flavor_text=None,
        set="NEO",
    )

    assert card.format_as_card() == expected_str
