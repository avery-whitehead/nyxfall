#!/usr/bin/env python
import argparse
from nyxfall.scryfall_requester import search_exact, search_random


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
        print(search_random().format_as_card(ascii_only=args.ascii))
    elif args.exact:
        card = search_exact(args.query)
        if card is not None:
            print(card.format_as_card(ascii_only=args.ascii))
        else:
            print(f"Card with name '{args.query}' not found")


if __name__ == "__main__":
    main()
