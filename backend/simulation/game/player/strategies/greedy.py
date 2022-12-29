import random
import copy
from itertools import permutations
from simulation.deck.card import Card
from simulation.deck.deck import Deck
from simulation.game.player.strategy import Strategy
from simulation.game.state.game_state import GameState
from simulation.game.state.player_state import PlayerState
from simulation.game_config.configs import GameConfig
from simulation.game_config.enums import StrategyType
from simulation.game_config.configs import GameConfig


class GreedyStrategy(Strategy):
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
        to_collect: dict[int, list[Card]] = game_state.to_collect_by_id[1]
        all_cards_to_collect: list[Card] = [card for cards in to_collect.values() for card in cards]
        
        my_deck: Deck = game_state.players_states[self.id].deck
        other_players: list[PlayerState] = [x for i, x in enumerate(game_state.players_states) if i!=self.id]

        if len(other_players) > 1:
            raise NotImplementedError

        if all(len(my_deck.cards) >= len(other_player.deck.cards) for other_player in other_players):
            random.shuffle(all_cards_to_collect)
            return all_cards_to_collect
        else:
            return self.select_best_permutation(game_state.players_states[self.id], other_players, all_cards_to_collect)

    def select_best_permutation(self, own_state: PlayerState, other_players: list[PlayerState], cards_to_collect: list[Card]) -> list[Card]:
        best_cards_amounts: int = -1
        best_order: list[Card] = []
        cards_to_collect_reducted: list[Card] = copy.deepcopy(cards_to_collect)


        opponent_deck: list[Card] = copy.deepcopy(other_players[0].deck.cards[len(own_state.deck.cards): min(len(own_state.deck.cards) + len(cards_to_collect), other_players[0].deck.size)])

        length_of_permutation: int  = min(len(opponent_deck), len(cards_to_collect_reducted), 6)

        for to_collect in permutations(cards_to_collect_reducted, length_of_permutation):
            other_deck = opponent_deck
            
            can_collect: int = self.max_card_to_take(list(to_collect), other_deck, length_of_permutation)

            if can_collect > best_cards_amounts:
                best_cards_amounts = can_collect
                best_order = list(to_collect)
            
            if best_cards_amounts == length_of_permutation:
                # we wont get better card layout
                break
        best_order[len(best_order):] = set(cards_to_collect_reducted) - set(best_order)
        return best_order

    def select_best_permutation_with_reduction(self, own_state: PlayerState, other_players: list[PlayerState], cards_to_collect: list[Card]) -> list[Card]:
        best_cards_amounts: int = -1
        best_order: list[Card] = []
        cards_to_collect_reducted: list[Card] = copy.deepcopy(cards_to_collect)


        max_to_collect: int = max(cards_to_collect).weight
        cards_to_collect_multiset: list[Card] = copy.deepcopy(sorted(cards_to_collect))
        opponent_deck: list[Card] = copy.deepcopy(other_players[0].deck.cards[len(own_state.deck.cards): min(len(own_state.deck.cards) + len(cards_to_collect), other_players[0].deck.size)])
        opponent_deck_multiset: list[Card] = copy.deepcopy(sorted(opponent_deck))
        reduction_dict: dict[int, Card] = {}
        while len(opponent_deck_multiset) > 0 and opponent_deck_multiset[-1].weight > max_to_collect:
            tmp = opponent_deck.index(opponent_deck_multiset[-1])
            reduction_dict[tmp] = cards_to_collect_multiset[0]
            opponent_deck_multiset.remove(opponent_deck_multiset[-1])
            cards_to_collect_multiset.remove(cards_to_collect_multiset[0])

        reduction_dict = dict(sorted(reduction_dict.items()))
        for x in reversed(reduction_dict):
            cards_to_collect_reducted.remove(reduction_dict[x])
            opponent_deck.pop(x)
        

        length_of_permutation: int  = min(len(opponent_deck), len(cards_to_collect_reducted), 6)

        for to_collect in permutations(cards_to_collect_reducted, length_of_permutation):
            other_deck: list[Card] = opponent_deck
            
            can_collect: int = self.max_card_to_take(list(to_collect), other_deck, length_of_permutation)
            
            if can_collect > best_cards_amounts:
                best_cards_amounts = can_collect
                best_order = list(to_collect)
            
            if best_cards_amounts == length_of_permutation:
                # we wont get better card layout
                break
        best_order[len(best_order):] = set(cards_to_collect_reducted) - set(best_order)
        for x in reduction_dict:
            best_order.insert(x, reduction_dict[x])
        return best_order

    def max_card_to_take(self, my_deck: list[Card], opponent_deck: list[Card], cards_to_check: int) -> int:
        can_collect: int = 0
        buffer_size: int = 1
        visible_card: bool = True
        
        # check how many cards we can take with this permutation 
        for i, x in enumerate(my_deck[:cards_to_check]):
            if not visible_card:
                buffer_size += 1
                visible_card = True
                continue
            if x == opponent_deck[i]:
                buffer_size += 1
                visible_card = False
            elif x > opponent_deck[i]:
                can_collect += buffer_size
                buffer_size = 1
            else:
                buffer_size = 1
        return can_collect
    
    def max_card_to_take_and_min_to_give(self, my_deck: list[Card], opponent_deck: list[Card], cards_to_check: int) -> float:
        can_collect: float = 0
        buffer_size: int = 1
        visible_card: bool = True
        
        # check how many cards we can take with this permutation 
        for i, x in enumerate(my_deck[:cards_to_check]):
            if not visible_card:
                buffer_size += 1
                visible_card = True
                continue
            if x == opponent_deck[i]:
                buffer_size += 1
                visible_card = False
            elif x > opponent_deck[i]:
                can_collect += buffer_size
                buffer_size = 1
            else:
                for j in range(buffer_size):
                    can_collect -= opponent_deck[i - j].weight * 0.0001
                buffer_size = 1
        return can_collect
