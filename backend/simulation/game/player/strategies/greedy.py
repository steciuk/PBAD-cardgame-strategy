import random
import copy
import numpy as np
from typing import Type
from itertools import permutations
from simulation.deck.card import Card
from simulation.deck.deck import Deck
from simulation.game.player.strategy import Strategy
from simulation.game.state.game_state import GameState
from simulation.game.state.player_state import PlayerState
from simulation.game_config.configs import GameConfig
from simulation.game_config.enums import StrategyType, CardsDistribution
from simulation.game_config.configs import GameConfig, PlayerConfig
# from simulation.game.game import Game
from simulation.game.simulator import SimulatorV2
from simulation.game.player.strategies.random_players import RandomPlayersStrategy
from simulation.game.player.strategies.random_cards import RandomCardsStrategy

# from simulation.game.player.map import StrategiesMap


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
        # print("collect greedy")
        to_collect: dict[int, list[Card]] = game_state.to_collect_by_id[1]
        all_cards_to_collect: list[Card] = [card for cards in to_collect.values() for card in cards]
        
        # print(game_state.players_states)
        
        my_deck: Deck = game_state.players_states[self.id].deck
        other_players: list[PlayerState] = [x for i, x in enumerate(game_state.players_states) if i!=self.id]

        if len(other_players) > 1:
            raise NotImplementedError

        if all(len(my_deck.cards) >= len(other_player.deck.cards) for other_player in other_players):
            random.shuffle(all_cards_to_collect)
            return all_cards_to_collect
        else:
            return self.select_best_permutation(game_state.players_states[self.id], other_players, all_cards_to_collect)
        # other_cards = [card for id in player_ids for card in to_collect[id] if id != self.id]

    def select_best_permutation(self, own_state: PlayerState, other_players: list[PlayerState], cards_to_collect: list[Card]) -> list[Card]:
        best_cards_amounts = -1
        best_order: list[Card] = []

        other_players_copy1 = copy.deepcopy(other_players)
        own_state_copy1 = copy.deepcopy(own_state)

        

        length_of_permutation: int  = min(len(other_players[0].deck.cards[len(own_state.deck.cards):]), len(cards_to_collect), 8)

        for to_collect in permutations(cards_to_collect, length_of_permutation):
            other_deck = other_players[0].deck.cards[len(own_state.deck.cards):]
            own_deck = cards_to_collect
            # assert len(other_deck) == len(other_players_copy1[0].deck.cards[len(own_state.deck.cards):])
            # assert len(own_deck) == len(cards_to_collect)
            
            can_collect: int = 0
            buffer_size: int = 1
            visible_card: bool = True
            
            # check how many cards we can take with this permutation 
            for i, x in enumerate(to_collect):
                if not visible_card:
                    buffer_size += 1
                    visible_card = True
                    continue
                if x == other_deck[i]:
                    buffer_size += 1
                    visible_card = False
                elif x > other_deck[i]:
                    can_collect += buffer_size
                    buffer_size = 1
                else:
                    buffer_size = 1

            # print(can_collect, to_collect)
            if can_collect > best_cards_amounts:
                best_cards_amounts = can_collect
                best_order = list(to_collect)
            
            if best_cards_amounts == length_of_permutation:
                # we wont get better card layout
                break
        best_order[len(best_order):] = set(cards_to_collect) - set(best_order)
        return best_order

