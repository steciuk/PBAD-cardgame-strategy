from strategy.card import Card
from strategy.deck import Deck


def main() -> None:
    deck = Deck()
    deck.full()
    deck.shuffle()
    print(deck.cards)


if __name__ == "__main__":
    main()
