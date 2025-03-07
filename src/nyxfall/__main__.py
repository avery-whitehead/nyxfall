#!/usr/bin/env python
import argparse
from beaupy import select  # type: ignore
from beaupy.spinners import Spinner  # type: ignore
from nyxfall.card import Card
from nyxfall.scryfall_requester import search_exact, search_query, search_random


def main():
    args = parse_args()
    run_cli(args)


def parse_args() -> argparse.Namespace:
    """Parses CLI arguments

    Returns:
        ``argparse.Namespace`` dictionary of arguments and their values
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("query", help="query to run against Scryfall", nargs="?")
    parser.add_argument(
        "-e",
        "--exact",
        help="try and match the query with an exact card name",
        action="store_true",
    )
    parser.add_argument(
        "-r", "--random", help="fetch a random card", action="store_true"
    )
    parser.add_argument(
        "-a",
        "--ascii",
        help="renders the card frame using only basic ASCII characters",
        action="store_true",
    )
    return parser.parse_args()


def run_cli(args: argparse.Namespace):
    """Runs the CLI application based on the arguments provided"""
    if not args.query and not args.random:
        print("You must either supply a query or use the --random flag")
    elif args.random:
        print(search_random().format_as_card(ascii_only=args.ascii))
    elif args.exact:
        card = search_exact(args.query)
        if card is not None:
            print(card.format_as_card(ascii_only=args.ascii))
        else:
            print(f"Could not find a card with the name '{args.query}'")
    else:
        spinner = Spinner(text="Fetching cards")
        spinner.start()
        cards = search_query(args.query)
        spinner.stop()
        if len(cards) == 1:
            print(cards[0].format_as_card(ascii_only=args.ascii))
        elif cards:
            selected_card: Card = select(
                options=cards,  # type: ignore
                preprocessor=lambda card: card.name,
                pagination=True,
                page_size=7,
            )
            print(selected_card.format_as_card(ascii_only=args.ascii))
        else:
            print(f"Could not find any cards matchng the query '{args.query}'")


if __name__ == "__main__":
    main()
