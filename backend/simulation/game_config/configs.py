import json
from typing import Any, Union

from simulation.game_config.enums import CardsDistribution, DeckType, Strategy


class PlayerConfig:
    def __init__(self, strategy: Strategy, cards:  Union[DeckType, list[str], None]) -> None:
        self.strategy: Strategy = strategy
        self.cards: DeckType | list[str] | None = cards


class RulesConfig:
    def __init__(self, num_cards_in_war: int) -> None:
        self.num_cards_in_war: int = num_cards_in_war


class GameConfig:
    def __init__(
            self,
            seed: Union[int, None],
            max_turns: Union[int, None],
            cards_distribution: CardsDistribution,
            deck: Union[DeckType, list[str], None],
            players: list[PlayerConfig],
            rules: RulesConfig) -> None:
        self.seed: int | None = seed
        self.max_turns: int | None = max_turns
        self.cards_distribution: CardsDistribution = cards_distribution
        self.deck: DeckType | list[str] | None = deck
        self.players: list[PlayerConfig] = players
        self.rules: RulesConfig = rules
