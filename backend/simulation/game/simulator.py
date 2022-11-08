from collections import defaultdict
from copy import deepcopy
from typing import Optional

from simulation.deck.card import Card
from simulation.game.state.game_state import GameState
from simulation.game.state.player_state import PlayerState
from simulation.game_config.configs import GameConfig, RulesConfig
from simulation.utils.state.init_player_state import init_player_states

# class TurnResult:
#     def __init__(self, winner_id: int, to_collect: dict[int, list[Card]]) -> None:
#         self.winner_id: int = winner_id
#         self.to_collect: dict[int, list[Card]] = to_collect


# class SimulatorState(Enum):
#     INIT_INPUT_CARDS = 'INIT_INPUT_CARDS'
#     INPUT_CARDS = 'INPUT_CARDS'
#     INPUT_WAR = 'INPUT_WAR'
#     RECEIVE_RESULT = 'RECEIVE_RESULT'


# class Simulator:
#     def __init__(
#         self,
#         rules_config: RulesConfig,
#         to_collect: defaultdict[int, list[Card]] = defaultdict(list),
#         state: SimulatorState = SimulatorState.INIT_INPUT_CARDS,
#         winner_id: Union[int, None] = None,
#         # fighting_players_ids: list[int] = [] TODO: analyze if needed
#     ) -> None:
#         self._rules_config: RulesConfig = rules_config
#         self._to_collect: defaultdict[int, list[Card]] = to_collect
#         self._state: SimulatorState = state
#         self._winner_id: Union[int, None] = winner_id
#         # self._fighting_players_ids: list[int] = fighting_players_ids

#     @property
#     def state(self) -> SimulatorState:
#         return self._state

#     def input_cards(self, cards_per_player: dict[int, Card]) -> list[int]:
#         """
#         Step the simulation by inputting the cards played by each player.
#         Simulation will be in 'RECEIVE_RESULT' or 'INPUT_WAR' state after this call.

#         Args:
#             cards_per_player (dict[int, Card]): dict of player id to card played by that player

#         Raises:
#             ValueError: if the simulator is not in the 'INPUT_CARDS' state

#         Returns:
#             list[int]: list of player ids that take part in the war (if any)
#         """
#         if self._state != SimulatorState.INIT_INPUT_CARDS and self._state != SimulatorState.INPUT_CARDS:
#             raise ValueError(f"Simulator is not in '{SimulatorState.INPUT_CARDS.name}' state.")

#         self._to_collect = defaultdict(list)
#         for player_id, card in cards_per_player.items():
#             self._to_collect[player_id].append(card)

#         return self._compare_cards(cards_per_player)

#     def input_war(self, cards_per_player: dict[int, list[Card]]) -> list[int]:
#         """
#         Step the simulation by inputting the cards added by each player to the war.

#         Args:
#             cards_per_player (dict[int, list[Card]]): dict of player id to cards added by that player

#         Raises:
#             ValueError: if the simulator is not in the 'INPUT_WAR' state

#         Returns:
#             list[int]: list of player ids that take part in the war (if any)

#         """
#         if self._state != SimulatorState.INPUT_WAR:
#             raise ValueError(f"Simulator is not in '{SimulatorState.INPUT_WAR.name}' state.")

#         fighting_cards: dict[int, Card] = {}

#         for player_id, cards in cards_per_player.items():
#             self._to_collect[player_id].extend(cards)
#             if len(cards) == self._rules_config.num_cards_in_war:
#                 fighting_cards[player_id] = cards[-1]

#         return self._compare_cards(fighting_cards)

#     def get_last_turn_result(self) -> TurnResult:
#         """
#         Receive the result of the last turn.
#         If simulation in 'RECEIVE_RESULT' must be called at least once to step the simulation.
#         Simulation will be in 'INPUT_CARDS' state after this call.

#         Raises:
#             ValueError: if the simulation is during the turn, or before the first turn

#         Returns:
#             FightResult: object containing the winner id and the dict of player id to cards collected by that player
#         """
#         if (self._state != SimulatorState.RECEIVE_RESULT and self._state != SimulatorState.INPUT_CARDS) or self._winner_id is None:
#             raise ValueError(
#                 f"Simulator is neither in '{SimulatorState.RECEIVE_RESULT.name}' nor in '{SimulatorState.INPUT_CARDS.name}' state."
#             )

#         self._state = SimulatorState.INPUT_CARDS
#         return TurnResult(self._winner_id, self._to_collect)

#     def clone(self) -> 'Simulator':
#         return Simulator(
#             self._rules_config,
#             self._to_collect,
#             self._state,
#             self._winner_id,
#             # self._fighting_players_ids
#         )

#     def _compare_cards(self, cards_per_player: dict[int, Card]) -> list[int]:
#         highest_card: Card = max(cards_per_player.items(), key=lambda x: x[1])[1]
#         fighting_players_ids = [
#             i for i, card in cards_per_player.items() if card.is_same_rank(highest_card)
#         ]

#         if len(fighting_players_ids) == 1:
#             self._winner_id = fighting_players_ids[0]
#             # self._fighting_players_ids = []
#             self._state = SimulatorState.RECEIVE_RESULT
#             return []

#         # self._fighting_players_ids = fighting_players_ids
#         self._state = SimulatorState.INPUT_WAR
#         return fighting_players_ids


class SimulatorV2:
    def __init__(self, game_config: GameConfig, game_state: GameState) -> None:
        self._game_config: GameConfig = game_config
        self._game_state: GameState = deepcopy(game_state)

    @property
    def game_state(self) -> GameState:
        return deepcopy(self._game_state)

    def turn(self, collect_order: Optional[list[Card]]) -> GameState:
        if self._game_state.to_collect is not None:
            if collect_order is None:
                raise ValueError('Game state requires card collection, but no collection order was provided.')

            # TODO: maybe check if the cards are the same

            self._game_state.players_states[self._game_state.to_collect[0]].deck.push_bottom(collect_order)
            self._game_state.to_collect = None

        players_in_game_ids: list[int] = []
        for player_state in self._game_state.players_states.values():
            if player_state.deck.size == 0:
                player_state.lost = True
            else:
                players_in_game_ids.append(player_state.id)

        if len(players_in_game_ids) == 1:
            self._game_state.winner_id = players_in_game_ids[0]  # only one player left
            return self.game_state
        if len(players_in_game_ids) == 0:
            self._game_state.winner_id = -1  # draw
            return self.game_state

        if self._game_config.max_turns is not None and self._game_state.turn >= self._game_config.max_turns:
            self._game_state.winner_id = -2  # max_turns reached
            return self.game_state

        to_collect: defaultdict[int, list[Card]] = defaultdict(list)
        self._game_state.turn += 1

        while True:  # TODO: not the cleanest loop condition but good for now xD
            fighting_cards: dict[int, Card] = {}
            for player_id, player_state in self._game_state.players_states.items():
                if not player_state.lost:
                    card: Card = self._game_state.players_states[player_id].deck.pop_top()
                    fighting_cards[player_id] = card
                    to_collect[player_id].append(card)

            highest_card: Card = max(fighting_cards.values())
            players_in_war: list[int] = [
                i for i, card in fighting_cards.items() if card.is_same_rank(highest_card)
            ]

            if len(players_in_war) == 1:
                self._game_state.to_collect = (players_in_war[0], to_collect)
                return self.game_state

            for player_in_war in players_in_war:
                player_in_war_state: PlayerState = self._game_state.players_states[player_in_war]
                if player_in_war_state.deck.size < self._game_config.rules.num_cards_in_war - 1:
                    to_collect[player_in_war].extend(player_in_war_state.deck.pop_all())
                    player_in_war_state.lost = True
                else:
                    to_collect[player_in_war].extend(
                        player_in_war_state.deck.pop_n_top(self._game_config.rules.num_cards_in_war)
                    )
