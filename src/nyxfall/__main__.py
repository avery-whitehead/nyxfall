#!/usr/bin/env python
import argparse
from beaupy import select  # type: ignore
from beaupy.spinners import *  # type: ignore
from nyxfall.card import Card
import nyxfall.scryfall_requester


def main():
    args = parse_args()
    run_cli(args)


def parse_args() -> argparse.Namespace:
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
    if not args.query and not args.random:
        print("You must either supply a query or use the --random flag")
    elif args.random:
        print(
            nyxfall.scryfall_requester.search_random().format_as_card(
                ascii_only=args.ascii
            )
        )
    elif args.exact:
        card = nyxfall.scryfall_requester.search_exact(args.query)
        if card is not None:
            print(card.format_as_card(ascii_only=args.ascii))
        else:
            print(f"Card with name '{args.query}' not found")
    else:
        spinner = Spinner()
        spinner.start()
        cards = nyxfall.scryfall_requester.search_query(args.query).data
        spinner.stop()
        selected_card: Card = select(
            options=cards,  # type: ignore
            preprocessor=lambda card: card.name,
            pagination=True,
            page_size=7,
        )

        print(selected_card.format_as_card())


if __name__ == "__main__":
    main()
