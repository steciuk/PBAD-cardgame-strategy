import copy
import random
import math
from simulation.deck.card import Card
from simulation.game.state.game_state import GameState
from simulation.game.state.player_state import PlayerState
from simulation.game_config.configs import GameConfig
from simulation.game_config.enums import StrategyType
from simulation.game.player.strategies.greedy import GreedyStrategy

PERMUTATIONS_NUMBER = 100

class GreedyRandomPermutations_100(GreedyStrategy):
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
        best_cards_amounts = -1
        best_order: list[Card] = []

        opponent_deck: list[Card] = other_players[0].deck.cards[len(own_state.deck.cards): min(
            len(own_state.deck.cards) + len(cards_to_collect), len(other_players[0].deck.cards))]
        length_of_permutation: int = min(len(opponent_deck), len(cards_to_collect))

        to_collect = copy.deepcopy(cards_to_collect)

        if math.factorial(length_of_permutation) <= PERMUTATIONS_NUMBER:
            # check all permutations
            return super().select_best_permutation(own_state, other_players, cards_to_collect)

        random.shuffle(to_collect)
        for _ in range(PERMUTATIONS_NUMBER):
            other_deck = opponent_deck

            # can_collect: int = self.max_card_to_take(list(to_collect), other_deck, length_of_permutation)
            can_collect: float = self.max_card_to_take_and_min_to_give(list(to_collect), other_deck, length_of_permutation)

            if can_collect > best_cards_amounts:
                best_cards_amounts = can_collect
                best_order = list(to_collect)
            random.shuffle(to_collect)
        return best_order
