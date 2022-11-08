from simulation.deck.deck import Deck
from simulation.game.state.player_state import PlayerState
from simulation.game_config.configs import GameConfig
from simulation.game_config.enums import CardsDistribution, DeckType
from simulation.utils.deck.utils import codes_to_cards, get_cards_list_of_type


def init_player_states(config: GameConfig) -> list[PlayerState]:
    players: list[PlayerState] = []
    num_players: int = len(config.players)

    if config.cards_distribution == CardsDistribution.RANDOM:
        if isinstance(config.deck, DeckType):
            deck: Deck = Deck(get_cards_list_of_type(config.deck))
        elif isinstance(config.deck, list):
            deck = Deck(codes_to_cards(config.deck))
        else:
            raise ValueError("Invalid config.")

        deck.shuffle()
        num_cards_per_player: int = deck.size // num_players
        cards_left: int = deck.size % num_players
        if cards_left != 0:
            print(f"Cannot distribute full deck equally. {cards_left} cards left unused.")

        for i, player_config in enumerate(config.players):
            players.append(PlayerState(i, Deck(deck.pop_n_top(num_cards_per_player)), player_config.strategy))

    elif config.cards_distribution == CardsDistribution.FIXED or config.cards_distribution == CardsDistribution.FIXED_RANDOM:
        for i, player_config in enumerate(config.players):
            if isinstance(player_config.cards, list):
                deck = Deck(codes_to_cards(player_config.cards))
                if config.cards_distribution == CardsDistribution.FIXED_RANDOM:
                    deck.shuffle()
                players.append(PlayerState(i, deck, player_config.strategy))
            elif isinstance(player_config.cards, DeckType):
                deck = Deck(get_cards_list_of_type(player_config.cards))
                if config.cards_distribution == CardsDistribution.FIXED_RANDOM:
                    deck.shuffle()
                players.append(PlayerState(i, deck, player_config.strategy))
            else:
                raise ValueError("Invalid config.")

    return players
