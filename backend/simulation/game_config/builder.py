from typing import Union

from simulation.game_config.configs import GameConfig, PlayerConfig, RulesConfig
from simulation.game_config.enums import CardsDistribution, DeckType, Strategy


class GameConfigBuilder():
    def __init__(self) -> None:
        self._seed: Union[int, None] = None
        self._max_turns: Union[int, None] = None
        self._cards_distribution = CardsDistribution.RANDOM
        self._deck: Union[DeckType, list[str], None] = DeckType.FULL
        self._players: list[PlayerConfig] = [
            PlayerConfig(Strategy.OWN_FIRST, None),
            PlayerConfig(Strategy.OWN_FIRST, None)]
        self._rules: RulesConfig = RulesConfig(1)

    def with_seed(self, seed: int) -> 'GameConfigBuilder':
        self._seed = seed
        return self

    def with_max_turns(self, max_turns: int) -> 'GameConfigBuilder':
        self._max_turns = max_turns
        return self

    def with_cards_distribution(self, cards_distribution: CardsDistribution) -> 'GameConfigBuilder':
        self._cards_distribution = cards_distribution
        return self

    def with_deck(self, deck: Union[DeckType, list[str]]) -> 'GameConfigBuilder':
        self._deck = deck
        return self

    def with_players(self, players: list[PlayerConfig]) -> 'GameConfigBuilder':
        self._players = players
        return self

    def with_rules(self, rules: RulesConfig) -> 'GameConfigBuilder':
        self._rules = rules
        return self

    def build(self) -> GameConfig:
        if len(self._players) < 2:
            raise ValueError('At least 2 players are required')

        if self._cards_distribution == CardsDistribution.FIXED:
            print("Property 'cards_distribution' is set to 'FIXED'. 'deck' property will be ignored.")
            self._deck = None

            for player in self._players:
                if player.cards is None or (isinstance(player.cards, list) and len(player.cards) == 0):
                    raise ValueError(
                        "Property 'cards_distribution' is set to 'FIXED' and not all players have 'cards' property set.")

        if self._cards_distribution == CardsDistribution.RANDOM:
            if isinstance(self._deck, list) and len(self._deck) == 0:
                raise ValueError(
                    "Property 'cards_distribution' is set to 'RANDOM'. 'deck' property is an empty list.")

            print("Property 'cards_distribution' is set to 'RANDOM'. 'cards' property of each player will be ignored.")
            for player in self._players:
                player.cards = None

        return GameConfig(
            self._seed, self._max_turns, self._cards_distribution, self._deck, self._players,
            self._rules)
