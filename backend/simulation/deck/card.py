from simulation.utils.deck.consts import SUITS_SET, WEIGHTS


class Card:
    def __init__(self, *args: str) -> None:
        """
        Create new card: Card('2', 'H') or Card('2H') 
        """
        if len(args) == 2:
            rank, suit = args
        elif len(args) == 1:
            code = args[0]
            if len(code) != 2:
                raise ValueError(f'illegal card code: {code}')

            rank = code[0]
            suit = code[1]
        else:
            raise ValueError('illegal constructor arguments')

        weight = WEIGHTS.get(rank)

        if suit not in SUITS_SET or weight is None:
            raise ValueError(f'illegal card suit or rank: {rank}{suit}')

        self._suit = suit
        self._rank = rank
        self._weight = weight

    @property
    def suit(self) -> str:
        return self._suit

    @property
    def rank(self) -> str:
        return self._rank

    @property
    def weight(self) -> int:
        return self._weight

    @property
    def code(self) -> str:
        """
        Returns card code

        Returns:
            str: "rank" + "suit"
        """
        return f"{self._rank}{self._suit}"

    def is_same_rank(self, other: "Card") -> bool:
        """
        Checks if card has the same rank and suit

        Args:
            other (Card): card to compare with

        Returns:
            bool: true if cards have the same rank and suit
        """
        return self._rank == other._rank

    def __repr__(self) -> str:
        return self.code

    def __eq__(self, other: object) -> bool:
        return isinstance(other, Card) and self.code == other.code

    def __ne__(self, other: object) -> bool:
        return isinstance(other, Card) and self.code != other.code

    def __lt__(self, other: "Card") -> bool:
        return self._weight < other._weight

    def __le__(self, other: "Card") -> bool:
        return self._weight <= other._weight

    def __gt__(self, other: "Card") -> bool:
        return self._weight > other._weight

    def __ge__(self, other: "Card") -> bool:
        return self._weight >= other._weight

    def __hash__(self) -> int:
        return hash(self.code)
