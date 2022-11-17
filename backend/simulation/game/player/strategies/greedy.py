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

        if all(len(my_deck.cards) >= len(other_player.deck.cards) for other_player in other_players):
            random.shuffle(all_cards_to_collect)
            return all_cards_to_collect
        else:
            # print("select_best_permutation")
            print(all_cards_to_collect)
            return self.select_best_permutation(game_state.players_states[self.id], other_players, all_cards_to_collect)
        # other_cards = [card for id in player_ids for card in to_collect[id] if id != self.id]

    def select_best_permutation(self, own_state: PlayerState, other_players: list[PlayerState], cards_to_collect: list[Card]) -> list[Card]:
        best_cards_ammounts = -1
        best_order: list[Card] = []

        max_deck: int = 0

        other_players_copy1 = copy.deepcopy(other_players)
        own_state_copy1 = copy.deepcopy(own_state)
        for player in other_players_copy1:
            player.deck.pop_n_top(len(own_state_copy1.deck.cards))
            max_deck = max(max_deck, len(player.deck.cards))
        length_of_permutation: int  = min(len(cards_to_collect), max_deck)

        own_state_copy1.strategy = StrategyType.RANDOM_CARDS
        own_state_copy1.deck.pop_all()
        print(length_of_permutation)
        for to_collect in permutations(cards_to_collect, length_of_permutation):
            
            # other_players_copy = copy.deepcopy(other_players)
            # own_state_copy = copy.deepcopy(own_state)
            # # print("\nnext permutation")
            # for player in other_players_copy:
            #     # print(len(other_players_copy), "orginal player deck", to_collect, player.deck.cards)
            #     player.deck.pop_n_top(len(own_state_copy.deck.cards))
            #     # print(len(other_players_copy), "new player deck", to_collect, player.deck.cards)
            # # print("orginal own deck", own_state_copy.deck.cards)
            # own_state_copy.deck.pop_all()
            own_state_copy = copy.deepcopy(own_state_copy1)
            own_state_copy.deck.push_bottom(list(to_collect))
            # print("new own deck", own_state_copy.deck.cards)

            other_players_copy = copy.deepcopy(other_players_copy1)
            all_players = other_players_copy.copy()
            all_players.insert(0, own_state_copy)
            # other_players.insert(0, own_state)
            playersConfig = [PlayerConfig(x.strategy, [str(y) for y in x.deck.cards]) for x in other_players_copy]
            playersConfig.insert(0, PlayerConfig(own_state_copy.strategy, [str(x) for x in to_collect]))
            config = GameConfig(
                                players=
                                    # PlayerConfig(own_state.strategy, [str(x) for x in cards_to_collect]),
                                    playersConfig
                                ,
                                cards_distribution=CardsDistribution.FIXED,
                                max_turns=len(to_collect)
                            )
            # game = Game(config, debug=False)
            # game.play()
            game_state = GameState(all_players)
            game_state.to_collect_by_id[0]
            simulator = SimulatorV2(config, game_state)

            player_strategies: dict[int, Strategy] = {}
            for player_state in game_state.players_states:
                strategy = RandomPlayersStrategy
                player_strategies[player_state.id] = strategy(player_state.id, config)
            # print("strategies", player_strategies)


            for _ in range(len(cards_to_collect) + 1):
                collected_cards: list[Card] = []
                # print("game_state.to_collect_by_id[0]", game_state.to_collect_by_id[0])
                if game_state.to_collect_by_id[0] is not None:
                    collected_cards = player_strategies[
                        game_state.to_collect_by_id[0]
                    ].collect(game_state)
                # print("collected_cards", collected_cards)
                game_state = simulator.turn(collected_cards)


            # print("own", game_state.players_states[0].deck.cards)
            # print("enemy", game_state.players_states[1].deck.cards)
            if len(game_state.players_states[0].deck.cards) > best_cards_ammounts:
                best_cards_ammounts = len(game_state.players_states[0].deck.cards)
                best_order = list(to_collect)
        best_order[len(best_order):] = set(cards_to_collect) - set(best_order)
        return best_order

# def get_strategy(strategy_type: StrategyType) -> Type[Strategy]:
#     strategy: Type[Strategy] | None = StrategiesMap.get(strategy_type)
#     if strategy is None:
#         raise ValueError(f"Strategy {strategy_type} not found")

#     return strategy

# StrategiesMap: dict[StrategyType, Type[Strategy]] = {
#     # StrategyType.OWN_FIRST: OwnFirstStrategy,
#     # StrategyType.OWN_LAST: OwnLastStrategy,
#     StrategyType.RANDOM_CARDS: RandomCardsStrategy,
#     StrategyType.RANDOM_PLAYERS: RandomPlayersStrategy,
#     StrategyType.GREEDY: GreedyStrategy,
# }