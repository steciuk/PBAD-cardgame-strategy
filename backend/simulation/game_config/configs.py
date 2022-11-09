from typing import Union

from simulation.game_config.enums import CardsDistribution, DeckType, StrategyType


class PlayerConfig:
    def __init__(self, strategy: StrategyType, cards: Union[DeckType, list[str], None] = None) -> None:
        self.strategy: StrategyType = strategy
        self.cards: DeckType | list[str] | None = cards


class RulesConfig:
    def __init__(self, num_cards_in_war: int = 1) -> None:
        if num_cards_in_war < 0:
            raise ValueError(f'num_cards_in_war must be non-negative, got {num_cards_in_war}')
        self.num_cards_in_war: int = num_cards_in_war


class GameConfig:
    def __init__(
            self, *,
            max_turns: Union[int, None] = None,
            cards_distribution: CardsDistribution = CardsDistribution.RANDOM,
            deck: Union[DeckType, list[str], None] = DeckType.FULL,
            players: list[PlayerConfig] = [PlayerConfig(StrategyType.OWN_FIRST, None), PlayerConfig(StrategyType.OWN_FIRST, None)],
            rules: RulesConfig = RulesConfig(1)) -> None:

        if len(players) < 2:
            raise ValueError('At least 2 players are required.')

        if cards_distribution == CardsDistribution.FIXED or cards_distribution == CardsDistribution.FIXED_RANDOM:
            print(
                f"Property 'cards_distribution' is set to '{cards_distribution.name}'. 'deck' property will be ignored."
            )
            deck = None

            for player in players:
                if player.cards is None or (isinstance(player.cards, list) and len(player.cards) == 0):
                    raise ValueError(
                        f"Property 'cards_distribution' is set to '{cards_distribution.name}' and not all players have 'cards' property set."
                    )

        elif cards_distribution == CardsDistribution.RANDOM:
            if deck is None:
                raise ValueError(
                    "Property 'cards_distribution' is set to 'RANDOM'. 'deck' property is None."
                )

            if isinstance(deck, list) and len(deck) == 0:
                raise ValueError(
                    "Property 'cards_distribution' is set to 'RANDOM'. 'deck' property is an empty list."
                )

            print("Property 'cards_distribution' is set to 'RANDOM'. 'cards' property of each player will be ignored.")
            for player in players:
                player.cards = None

        self.max_turns: int | None = max_turns
        self.cards_distribution: CardsDistribution = cards_distribution
        self.deck: DeckType | list[str] | None = deck
        self.players: list[PlayerConfig] = players
        self.rules: RulesConfig = rules
