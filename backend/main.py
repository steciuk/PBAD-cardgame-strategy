from strategy.card import Card
from strategy.deck import Deck


def war() -> None:
    deck = Deck()
    deck.full()
    deck.shuffle()
    players: tuple[Deck, Deck] = (Deck(deck.pop_n_top(26)), Deck(deck.cards))

    print(f'Player 1: {players[0]}')
    print(f'Weight: {players[0].weight}')
    print('')
    print(f'Player 2: {players[1]}')
    print(f'Weight: {players[1].weight}')
    print('--------------------------------------')

    wars: int = 0
    turn: int = 1
    longest_turn = 0

    turn_won: bool = False
    while players[0].size > 0 and players[1].size > 0:
        print(f'\nturn {turn}')
        turn += 1

        to_collect_0: list[Card] = []
        to_collect_1: list[Card] = []
        turn_length = 0
        turn_won = False

        while not turn_won:
            card_0 = players[0].pop_top()
            card_1 = players[1].pop_top()

            print(f'{card_0.rank} vs {card_1.rank}')
            if card_0 > card_1:
                players[0].push_bottom(
                    [*to_collect_0, *to_collect_1, card_0, card_1])

                turn_won = True
            elif card_0 < card_1:
                players[1].push_bottom(
                    [*to_collect_1, *to_collect_0, card_1, card_0]
                )

                turn_won = True
            else:
                if players[0].size < 3:
                    players[1].push_bottom(
                        [*to_collect_1, *to_collect_0, card_1, card_0, *players[0].cards])

                    turn_won = True
                    players[0].empty()

                elif players[1].size < 3:
                    players[0].push_bottom(
                        [*to_collect_0, *to_collect_1, card_0, card_1, *players[1].cards])

                    turn_won = True
                    players[1].empty()

                else:
                    wars += 1
                    turn_length += 1
                    longest_turn = max(longest_turn, turn_length)
                    to_collect_0.extend([card_0, *players[0].pop_n_top(2)])
                    to_collect_1.extend([card_1, *players[1].pop_n_top(2)])

    print('--------------------------------------')
    print(f'Player {0 if players[1].size == 0 else 1} won')
    print(f'Turns: {turn}')
    print(f'Wars: {wars}')
    print(f'Longest turn: {longest_turn} wars')


def main() -> None:
    pass


if __name__ == "__main__":
    war()
