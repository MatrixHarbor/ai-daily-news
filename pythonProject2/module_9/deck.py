import random
from card import Card

class OutOfCards(Exception):
    pass

class Deck:
    SUITS = ["Hearts", "Clubs", "Diamonds", "Spades"]
    CARDS = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]

    def __init__(self) -> None:
        """
        Creates a new deck of 52 cards.
        """
        self.cards = []
        for card in self.CARDS:
            for suit in self.SUITS:
                self.cards.append(Card(suit, card))
        self.shuffle()

    def shuffle(self) -> None:
        """
        Shuffles the deck.
        """
        random.shuffle(self.cards)

    def deal(self) -> None:
        """
        Deals a card from the deck.
        """
        try:
            return self.cards.pop()
        except IndexError:
            raise OutOfCards("No more cards in the deck!")

    def save(self, filename) -> None:
        """
        Saves the deck to a file.
        """
        with open(filename, "w") as file:
            for card in self.cards:
                file.write(f'{card}\n')

    def load(self, filename) -> None:
        """
        Loads the deck from a file.
        """
        self.cards = []
        with open(filename, "r") as file:
            for line in file:
                card, suit = line.strip().split(" of ")
                self.cards.append(Card(suit, card))

    def __str__(self) -> str:
        """
        Returns a string representation of the deck.
        """
        card_string = ""
        for card in reversed(self.cards):
            card_string += f'{card}\n'
        return card_string

    def __len__(self) -> int:
        """
        Returns the number of cards in the deck.
        """
        return len(self.cards)