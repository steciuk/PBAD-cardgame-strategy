from itertools import permutations
from simulation.deck.card import Card
from simulation.game.state.game_state import GameState
from simulation.game.state.player_state import PlayerState
from simulation.game_config.configs import GameConfig
from simulation.game_config.enums import StrategyType
from simulation.game.player.strategies.greedy import GreedyStrategy

class GreedyStrategyGroupedBy6(GreedyStrategy):
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

    def select_best_permutation(self, own_state: PlayerState, other_players: list[PlayerState], cards_to_collect: list[Card]) -> list[Card]:
        best_cards_amounts: int = -1
        best_order: list[Card] = []

        opponent_deck: list[Card] = other_players[0].deck.cards[len(own_state.deck.cards): len(own_state.deck.cards) + len(cards_to_collect)]

        just_collected: int = 0

        while just_collected < len(cards_to_collect) and just_collected < len(opponent_deck):
            length_of_permutation: int  = min(len(opponent_deck) - just_collected, len(cards_to_collect) - just_collected, 6)
            for to_collect in permutations(cards_to_collect[just_collected: just_collected + length_of_permutation]):
                other_deck = opponent_deck
                
                can_collect: int = self.max_card_to_take(list(to_collect), other_deck, length_of_permutation)

                if can_collect > best_cards_amounts:
                    best_cards_amounts = can_collect
                    best_order = list(to_collect)
                
                if best_cards_amounts == length_of_permutation:
                    # we wont get better card layout
                    break
            just_collected += length_of_permutation
            # if just_collected > 2: 
            #     print(just_collected)
        best_order[len(best_order):] = set(cards_to_collect) - set(best_order)

        return best_order

