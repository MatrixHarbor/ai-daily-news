from player import Player


class Counter(Player):
    def __init__(self, deck):
        # Initialize a Counter with a deck and a starting count of 0.
        super().__init__(deck)
        self.count = 0

    def play(self):
        # Determines whether to hit or stay based on the current count.
        # Hits if the count is above 0, stays otherwise.
        if self.count > 0:
            return self.hit()
        else:
            return self.stay()

    def update_count(self, card):
        # Updates the count based on the value of the card drawn.
        value = card.get_point_value()

        if isinstance(value, tuple):  # Ace
            self.count -= 1
        elif value == 10:  # Face card or 10
            self.count -= 1
        elif 2 <= value <= 6:  # Low cards (2-6)
            self.count += 1

    def __str__(self):
        return "Counter"