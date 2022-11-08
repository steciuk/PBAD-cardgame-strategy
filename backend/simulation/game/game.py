from collections import defaultdict

from simulation.deck.card import Card
from simulation.deck.deck import Deck
from simulation.game.player.map import PlayersMap
from simulation.game.player.player import Player
from simulation.game.simulator import SimulatorV2
from simulation.game_config.configs import GameConfig
from simulation.game_config.enums import CardsDistribution, DeckType
from simulation.utils.deck.utils import codes_to_cards, get_cards_list_of_type
from simulation.utils.state.init_player_state import init_player_states


class Game():
    def __init__(self, config: GameConfig) -> None:
        self._config: GameConfig = config
        self._num_players: int = len(config.players)
        self._players: dict[int, Player] = {}

    def play(self) -> None:
        pass
