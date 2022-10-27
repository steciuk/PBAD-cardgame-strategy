from enum import Enum


class CardsDistribution(Enum):
    RANDOM = 'RANDOM'
    FIXED = 'FIXED'


class DeckType(Enum):
    FULL = 'FULL'
    RED = 'RED'
    BLACK = 'BLACK'
    SPADES = 'SPADES'
    CLUBS = 'CLUBS'
    DIAMONDS = 'DIAMONDS'
    HEARTS = 'HEARTS'


class Strategy(Enum):
    OWN_FIRST = 'OWN_FIRST'
