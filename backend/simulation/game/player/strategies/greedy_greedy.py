import copy
from simulation.deck.card import Card
from simulation.game.state.game_state import GameState
from simulation.game.state.player_state import PlayerState
from simulation.game_config.configs import GameConfig
from simulation.game_config.enums import StrategyType
from simulation.game.player.strategies.greedy import GreedyStrategy


class GreedyGreedy(GreedyStrategy):
    def __init__(self, id: int, game_config: GameConfig) -> None:
        super().__init__(id, game_config)

    @property
    def strategy_type(self) -> StrategyType:
        return StrategyType.GREEDY

    def collect(
        self,
        game_state: GameState
    ) -> list[Card]:
        """
        Collects 
        """
        return super().collect(game_state)

    def select_best_permutation(
            self, own_state: PlayerState, other_players: list[PlayerState],
            cards_to_collect: list[Card]) -> list[Card]:

        opponent_deck: list[Card] = other_players[0].deck.cards[len(own_state.deck.cards): min(
            len(own_state.deck.cards) + len(cards_to_collect), len(other_players[0].deck.cards))]

        to_collect_copy = copy.deepcopy(cards_to_collect)
        sorted_opponent_deck = sorted(opponent_deck, reverse=True)

        pairs = []

        for card in sorted_opponent_deck:
            if card > max(to_collect_copy):
                pairs.append((card, min(to_collect_copy)))
                to_collect_copy.remove(min(to_collect_copy))
            else:
                pairs.append((card, max(to_collect_copy)))
                to_collect_copy.remove(max(to_collect_copy))

        result = []
        pairs = dict(pairs)
        for x in opponent_deck:
            result.append(pairs[x])

        result[len(result):] = set(cards_to_collect) - set(result)

        return result
