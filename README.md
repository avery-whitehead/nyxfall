# nyxfall, a command-line Magic: the Gathering card search
![demo](https://github.com/user-attachments/assets/2bc7256a-cf40-47d5-b980-a3a5aabe01ae)

## Installation
### Using pip
```console
$ pip install nyxfall
```

### From source (requires Python 3.12.3 or greater)

(optional) Start a virtual environment

```console
$ python -m venv venv
$ source venv/bin/activate
```

Install the project with pip
```console
$ python -m pip install .
```

## Usage

```console
$ nyxfall -h
usage: nyxfall [-h] [-e] [-r] [-a] [query]

positional arguments:
  query         query to run against Scryfall

options:
  -h, --help    show this help message and exit
  -e, --exact   try and match the query with an exact card name
  -r, --random  fetch a random card
  -a, --ascii   renders the card frame using only basic ASCII characters
```

### Searching for a set of cards
If more than one card is returned from your search, use the arrow keys + enter to select which one to display
```console
$ nyxfall llanowar

  Llanowar Elite
> Llanowar Elves
  Llanowar Empath
  Llanowar Envoy
  Llanowar Greenwidow
  Llanowar Knight
  Llanowar Loamspeaker

Page 2/4

┌──────────────────────────────────┐
│┌────────────────────────────────┐│
││Llanowar Elves               {G}││
│└┬──────────────────────────────┬┘│
│ │                              │ │
│┌┴──────────────────────────────┴┐│
││Creature — Elf Druid            ││
│└┬──────────────────────────────┬┘│
│ │{T}: Add {G}.                 │ │
│ │ ──────────────────────────── │ │
│ │The elves of the Llanowar     │ │
│ │forest have defended it for   │ │
│ │generations. It is their      │ │
│ │sacred duty to keep outside   │ │
│ │influences from corrupting    │ │
│ │their ancestral home.         │ │
│ │                       ┌─────┐│ │
│ └───────────────────────┤ 1/1 ├┘ │
│ FDN                     └─────┘  │
└──────────────────────────────────┘
```

### Searching for an exact card
```console
$ nyxfall -e "force of negation"

┌──────────────────────────────────┐
│┌────────────────────────────────┐│
││Force of Negation      {1}{U}{U}││
│└┬──────────────────────────────┬┘│
│ │                              │ │
│┌┴──────────────────────────────┴┐│
││Instant                         ││
│└┬──────────────────────────────┬┘│
│ │If it's not your turn, you may│ │
│ │exile a blue card from your   │ │
│ │hand rather than pay this     │ │
│ │spell's mana cost.            │ │
│ │Counter target noncreature    │ │
│ │spell. If that spell is       │ │
│ │countered this way, exile it  │ │
│ │instead of putting it into its│ │
│ │owner's graveyard.            │ │
│ │ ──────────────────────────── │ │
│ │"Try, if you must."           │ │
│ └──────────────────────────────┘ │
│ 2X2                              │
└──────────────────────────────────┘
```

### Searching for a random card
```console
$ nyxfall -r

┌──────────────────────────────────┐
│┌────────────────────────────────┐│
││Helpful Hunter            {1}{W}││
│└┬──────────────────────────────┬┘│
│ │                              │ │
│┌┴──────────────────────────────┴┐│
││Creature — Cat                  ││
│└┬──────────────────────────────┬┘│
│ │When this creature enters,    │ │
│ │draw a card.                  │ │
│ │ ──────────────────────────── │ │
│ │"Ah, the conquering hero      │ │
│ │returns! What trials did you  │ │
│ │face, little one?"            │ │
│ │—Basri Ket                    │ │
│ │                       ┌─────┐│ │
│ └───────────────────────┤ 1/1 ├┘ │
│ FDN                     └─────┘  │
└──────────────────────────────────┘
```
