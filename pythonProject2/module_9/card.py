class Card:
    def __init__(self, suit, card) -> None:
        """
        Create a card instance by providing the suit and card.
        """
        self.suit = suit
        self.card = card

    def get_point_value(self) -> int | tuple:
        """
        Returns the point value of the card.
        """
        if self.card == "Ace":
            return (1, 11)
        elif self.card in ["Jack", "Queen", "King"]:
            return 10
        else:
            return int(self.card)

    def __str__(self) -> str:
        """
        Returns a string representation of the card.
        """
        return f"{self.card} of {self.suit}"