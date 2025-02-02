class Player:
    def __init__(self, deck):
        # Initialize a player with an empty hand and a deck to draw from.
        self.deck = deck
        self.clear_hand()

    def clear_hand(self):
        self.hand = []

    def print_hand(self):
        for card in self.hand:
            print(card)
        print(f"Score: {self.hand_value()}\n")

    def hit(self):
        card = self.deck.deal()
        self.hand.append(card)
        return card

    def stay(self):
        return "stay"

    def hand_value(self):
        total = 0
        aces = 0

        for card in self.hand:
            value = card.get_point_value()
            if isinstance(value, tuple):
                # Count aces separately
                aces += 1
                total += 11  # Assume Ace is worth 11 initially
            else:
                total += value

        # Adjust for Aces if the total exceeds 21
        while total > 21 and aces:
            total -= 10  # Convert an Ace from 11 to 1
            aces -= 1

        return total