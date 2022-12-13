import collections
from collections import defaultdict
from copy import deepcopy
from typing import Optional

from simulation.deck.card import Card
from simulation.game.state.game_state import GameState
from simulation.game.state.player_state import PlayerState
from simulation.game_config.configs import GameConfig


class SimulatorV2:
    def __init__(self, game_config: GameConfig, game_state: GameState) -> None:
        self._game_config: GameConfig = game_config
        self._game_state: GameState = deepcopy(game_state)

    @property
    def game_state(self) -> GameState:
        return deepcopy(self._game_state)

    def turn(self, collect_order: Optional[list[Card]] = None) -> GameState:
        if self._game_state.winner_id is not None:
            return self.game_state

        if self._game_state.to_collect_by_id[0] is not None:
            if collect_order is None:
                raise ValueError('Game state requires card collection, but no collection order was provided.')

            if collections.Counter(
                [card for cards in self._game_state.to_collect_by_id[1].values() for card in cards]
            ) != collections.Counter(collect_order):
                raise ValueError('Invalid strategy. Cards were not collected properly.')

            player_to_add_to: PlayerState | None = next(
                (player for player in self._game_state.players_states
                 if player.id == self._game_state.to_collect_by_id[0]), None
            )
            if player_to_add_to is None:
                raise ValueError('Player who should collect cards is not in the Game State.')

            player_to_add_to.deck.push_bottom(collect_order)
            self._game_state.to_collect_by_id = (None, {})

        if self._game_config.max_turns is not None and self._game_state.turn >= self._game_config.max_turns:
            self._game_state.winner_id = -2  # max_turns reached
            return self.game_state

        if collect_order != None and len(collect_order) in self._game_state.wars_number: 
            self._game_state.wars_number[len(collect_order)] += 1
        elif collect_order != None:
            self._game_state.wars_number[len(collect_order)] = 1

        to_collect: defaultdict[int, list[Card]] = defaultdict(list)
        self._game_state.turn += 1

        player_states_in_war: list[PlayerState] = [*self._game_state.players_states]

        while True:  # TODO: not the cleanest loop condition but good for now xD
            player_states_in_war = [
                player_state for player_state in player_states_in_war
                if player_state.deck.size > 0
            ]

            if len(player_states_in_war) < 2:
                player_states_in_game: list[PlayerState] = [
                    player_state for player_state in self._game_state.players_states
                    if player_state.deck.size > 0
                ]

                if len(player_states_in_war) == 1:
                    # one player left in this turn
                    if len(player_states_in_game) == 1 and len(to_collect) == 0:
                        # one player left in the game and there sre no cards to collect
                        # so this player won
                        self._game_state.winner_id = player_states_in_game[0].id
                    else:
                        # there is more than one player in the game or there are cards to collect
                        # so the player who won this turn should collect the cards
                        self._game_state.to_collect_by_id = (player_states_in_war[0].id, to_collect)

                    return self.game_state

                elif len(player_states_in_war) == 0:
                    # no players left in this turn, so they used all their cards, there won't be any cards to collect
                    if len(player_states_in_game) == 1:
                        # one player left in the game, so this player won
                        self._game_state.winner_id = player_states_in_game[0].id
                    elif len(player_states_in_game) == 0:
                        # no players left in the game, so it's a draw
                        self._game_state.winner_id = -1  # draw
                    else:
                        # there are more than one player left in the game
                        # so the game continues, without the cards used by players in a war
                        pass

                    return self.game_state

            fighting_cards: dict[int, Card] = {}
            for player_state in player_states_in_war:
                card: Card = player_state.deck.pop_top()
                fighting_cards[player_state.id] = card
                to_collect[player_state.id].append(card)

            highest_card: Card = max(fighting_cards.values())
            players_ids_in_war: list[int] = [
                i for i, card in fighting_cards.items() if card.is_same_rank(highest_card)
            ]

            if len(players_ids_in_war) == 1:
                self._game_state.to_collect_by_id = (players_ids_in_war[0], to_collect)
                return self.game_state

            player_states_in_war = [
                player_state for player_state in player_states_in_war
                if player_state.id in players_ids_in_war
            ]

            for player_state in player_states_in_war:
                if player_state.deck.size < self._game_config.rules.num_cards_in_war + 1:
                    to_collect[player_state.id].extend(player_state.deck.pop_all())
                else:
                    to_collect[player_state.id].extend(
                        player_state.deck.pop_n_top(self._game_config.rules.num_cards_in_war)
                    )
