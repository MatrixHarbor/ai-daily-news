from player import Player

class Dealer(Player):
    def play(self):
        """
        Dealer's play logic:
        - Hit on a score of 16 or lower.
        - Stay on a score of 17 or higher.
        """
        if self.hand_value() <= 16:
            return self.hit()
        else:
            return self.stay()

    def __str__(self):
        # Returns the string 'Dealer' to identify the player as the dealer.
        return "Dealer"