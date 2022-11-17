from collections import defaultdict

from simulation.deck.card import Card
from simulation.game.player.map import get_strategies_form_game_state
from simulation.game.player.strategy import Strategy
from simulation.game.simulator import SimulatorV2
from simulation.game.state.game_state import GameState
from simulation.game.state.player_state import PlayerState
from simulation.game_config.configs import GameConfig
from simulation.utils.state.init_player_state import init_players_states


class Game():
    game_state: GameState

    def __init__(self, config: GameConfig, *, debug: bool = False) -> None:
        self._config: GameConfig = config
        self._debug: bool = debug
        self.game_state: GameState = GameState([])

    def play(self) -> None:
        starting_player_states: list[PlayerState] = init_players_states(self._config)
        self.game_state: GameState = GameState(starting_player_states)
        player_strategies: dict[int, Strategy] = get_strategies_form_game_state(
            self.game_state, self._config
        )

        simulator = SimulatorV2(self._config, self.game_state)

        while self.game_state.winner_id is None:
            if self._debug:
                print(self.game_state)

            collected_cards: list[Card] = []
            if self.game_state.to_collect_by_id[0] is not None:
                collected_cards = player_strategies[
                    self.game_state.to_collect_by_id[0]
                ].collect(self.game_state)

            self.game_state = simulator.turn(collected_cards)

        if self._debug:
            print(self.game_state)
            if self.game_state.winner_id == -1:
                print('Draw')
            elif self.game_state.winner_id == -2:
                print('Max turns reached')
            else:
                print(f'Player: {self.game_state.winner_id} won!')
