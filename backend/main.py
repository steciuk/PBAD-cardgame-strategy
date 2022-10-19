from strategy.Deck import Deck


def main() -> None:
    deck = Deck()
    deck.full()
    deck.shuffle()
    print(deck.cards)


if __name__ == "__main__":
    main()
