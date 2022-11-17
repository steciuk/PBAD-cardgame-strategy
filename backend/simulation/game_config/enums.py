from enum import Enum


class CardsDistribution(Enum):
    RANDOM = 'RANDOM'
    FIXED = 'FIXED'
    FIXED_RANDOM = 'FIXED_RANDOM'


class DeckType(Enum):
    FULL = 'FULL'
    RED = 'RED'
    BLACK = 'BLACK'
    SPADES = 'SPADES'
    CLUBS = 'CLUBS'
    DIAMONDS = 'DIAMONDS'
    HEARTS = 'HEARTS'


class StrategyType(Enum):
    OWN_FIRST = 'OWN_FIRST'
    OWN_LAST = 'OWN_LAST'
    RANDOM_CARDS = 'RANDOM_CARDS'
    RANDOM_PLAYERS = 'RANDOM_PLAYERS'
    GREEDY = "GREEDY"
