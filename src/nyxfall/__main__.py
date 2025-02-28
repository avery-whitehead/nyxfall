#!/usr/bin/env python
import argparse
from nyxfall.scryfall_requester import search_exact, search_random


def main():
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
    args = parser.parse_args()

    if not args.query and not args.random:
        print("You must either supply a query or use the --random flag")
    elif args.random:
        search_random().print_as_card()
    elif args.exact:
        card = search_exact(args.query)
        if card is not None:
            card.print_as_card()
        else:
            print(f"Card with name '{args.query}' not found")


if __name__ == "__main__":
    main()
