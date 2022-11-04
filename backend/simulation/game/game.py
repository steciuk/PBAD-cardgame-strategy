from collections import defaultdict

from simulation.deck.card import Card
from simulation.deck.deck import Deck
from simulation.game.player.map import PlayersMap
from simulation.game.player.player import Player
from simulation.game_config.configs import GameConfig
from simulation.game_config.enums import CardsDistribution, DeckType
from simulation.utils.deck.utils import codes_to_cards, get_cards_list_of_type


class Game():
    def __init__(self, config: GameConfig) -> None:
        self._config: GameConfig = config
        self._num_players: int = len(config.players)
        self._players: dict[int, Player] = {}

    def play(self) -> None:
        self._initialize_players()
        for player in self._players.values():  # TODO: debug
            print(player._deck)

        wars: int = 0
        turn: int = 1
        turn_won: bool = False
        players_in_game: list[Player] = [*self._players.values()]

        while len(players_in_game) > 1 and (self._config.max_turns is None or turn <= self._config.max_turns):
            print(f'\nturn {turn}')
            turn += 1
            to_collect: defaultdict[int, list[Card]] = defaultdict(list)
            turn_won = False

            while not turn_won and len(players_in_game) > 1:
                fighting: dict[int, Card] = {}
                for player in players_in_game:
                    fighting[player.id] = player.play()

                print(' vs '.join([card.rank for card in fighting.values()]))

                highest_card = max(fighting.items(), key=lambda x: x[1])[1]
                fighting_players_ids: list[int] = [
                    i for i, card in fighting.items() if card.is_same_rank(highest_card)
                ]
                if len(fighting_players_ids) == 1:
                    turn_won = True
                    for i, card in fighting.items():
                        to_collect[i].append(card)
                        if i != fighting_players_ids[0] and self._players[i].num_cards == 0:
                            players_in_game.remove(self._players[i])

                    self._players[fighting_players_ids[0]].collect(to_collect)
                else:
                    wars += 1
                    for i, card in fighting.items():
                        to_collect[i].append(card)

                        if not self._players[i].can_war():
                            players_in_game.remove(self._players[i])

                        to_collect[i].extend(self._players[i].war())

        print(f'Turns: {turn}')
        print(f'Wars: {wars}')

        for player in self._players.values():  # TODO: debug
            print(player._deck)

    def _initialize_players(self) -> None:
        self._players = {}
        if self._config.cards_distribution == CardsDistribution.RANDOM:
            if isinstance(self._config.deck, DeckType):
                deck: Deck = Deck(get_cards_list_of_type(self._config.deck))
            elif isinstance(self._config.deck, list):
                deck = Deck(codes_to_cards(self._config.deck))
            else:
                raise ValueError("Invalid config.")

            deck.shuffle()
            num_cards_per_player: int = deck.size // self._num_players
            cards_left: int = deck.size % self._num_players
            if cards_left != 0:
                print(f"Cannot distribute full deck equally. {cards_left} cards left unused.")

            for i, player_config in enumerate(self._config.players):
                player_class = PlayersMap.get(player_config.strategy)
                if player_class is None:
                    raise ValueError(f"Nonexisting strategy: {player_config.strategy}.")

                self._players[i] = (player_class(i, Deck(deck.pop_n_top(num_cards_per_player)), self._config))

        elif self._config.cards_distribution == CardsDistribution.FIXED or self._config.cards_distribution == CardsDistribution.FIXED_RANDOM:
            for i, player_config in enumerate(self._config.players):
                player_class = PlayersMap.get(player_config.strategy)
                if player_class is None:
                    raise ValueError(f"Nonexisting strategy: {player_config.strategy}.")

                if isinstance(player_config.cards, list):
                    deck = Deck(codes_to_cards(player_config.cards))
                    if self._config.cards_distribution == CardsDistribution.FIXED_RANDOM:
                        deck.shuffle()
                    self._players[i] = (player_class(i, deck, self._config))
                elif isinstance(player_config.cards, DeckType):
                    deck = Deck(get_cards_list_of_type(player_config.cards))
                    if self._config.cards_distribution == CardsDistribution.FIXED_RANDOM:
                        deck.shuffle()
                    self._players[i] = (player_class(i, deck, self._config))
                else:
                    raise ValueError("Invalid config.")
