from dataclasses import dataclass

class game_state:
    profile_name: str
    deck_count: int
    card_orientation: str
    selected_decks: list[str]
    repeat: bool
    shuffle: bool

class card:
    front: str
    back: str
    id: str
    ratio: float

class deck:
    name: str
    cards: list[card]
    perfomance: float

