from deck import Deck, OutOfCards
from dealer import Dealer
from counter import Counter

class Blackjack:
    def __init__(self, deck=None) -> None:
        """
        Create a new blackjack game.
        """
        if deck:
            self.deck = deck
        else:
            self.deck = Deck()
        self.dealer = Dealer(self.deck)
        self.counter = Counter(self.deck)
        self.players = [self.counter, self.dealer]
        self.player_states = {self.dealer: "Playing", self.counter: "Playing"}
        self.winner = None
        self.wins = {self.dealer: 0, self.counter: 0}
        self.ties = 0

    def print_hands(self) -> None:
        """
        Prints the hands of all players.
        """
        for player in self.players:
            print(f'{player}:')
            player.print_hand()
            print()

    def setup_round(self) -> None:
        """
        Draw initial cards for the round and monitor for Blackjacks.
        """
        # Deal two cards to each player
        for _ in range(2):
            for player in self.players:
                result = player.hit()
                self.counter.update_count(result)

        # Check for blackjack if the player has exactly two cards
        for player in self.players:
            if len(player.hand) == 2:
                if (player.hand[0].card == "Ace" and player.hand[1].card in ["10", "Jack", "Queen", "King"]) or \
                        (player.hand[1].card == "Ace" and player.hand[0].card in ["10", "Jack", "Queen", "King"]):
                    self.blackjack(player)

    def play_round(self) -> None:
        """
        Play a round of blackjack.
        """
        if not self.winner:
            for player in self.players:
                action = ""
                while action != "stay" and self.player_states[player] == "Playing":
                    print(f"{player}'s turn.\n")
                    print("--Current Hand--")
                    player.print_hand()
                    print()
                    action = player.play()
                    print(f"{player} {action if action == 'stay' else 'hit'}.\n")
                    if action != "stay":
                        self.counter.update_count(action)
                        print("--Resulting Hand--")
                        player.print_hand()
                        print()
                    if player.hand_value() > 21:
                        self.bust(player)

    def score_round(self) -> None:
        """
        Score the round.
        """
        match (self.player_states[self.dealer], self.player_states[self.counter]):
            case ("Blackjack", "Blackjack"):
                self.tie()
            case ("Blackjack", "Playing"):
                self.win(self.dealer)
            case ("Playing", "Blackjack"):
                self.win(self.counter)
            case ("Bust", "Bust"):
                self.win(self.dealer)
            case ("Bust", "Playing"):
                self.win(self.counter)
            case ("Playing", "Bust"):
                self.win(self.dealer)
            case ("Playing", "Playing"):
                if self.dealer.hand_value() > self.counter.hand_value():
                    self.win(self.dealer)
                elif self.counter.hand_value() > self.dealer.hand_value():
                    self.win(self.counter)
                else:
                    self.tie()
            case _:
                import pdb; pdb.set_trace()
                raise Exception("Invalid state combination")

        if self.winner == self.dealer:
            print("Dealer wins!\n")
        elif self.winner == self.counter:
            print("Counter wins!\n")
        else:
            print("Tie!\n")

    def win(self, player) -> None:
        """
        Set the winner for the round
        """
        self.winner = player
        self.wins[player] += 1

    def tie(self) -> None:
        """
        Set the winner to None for a tie.
        """
        self.winner = None
        self.ties += 1

    def blackjack(self, player) -> None:
        """
        Sets the player's state to blackjack.
        """
        self.player_states[player] = "Blackjack"
        print(f"{player} BLACKJACK!")

    def bust(self, player) -> None:
        """
        Sets the player's state to bust.
        """
        self.player_states[player] = "Bust"
        print(f"{player} BUST!")

    def run(self):
        """
        Run the blackjack game.
        """
        round = 1
        try:
            while True:
                self.winner = None
                # Attempt to set up the round; if the deck is empty, catch the OutOfCards exception
                print(f'ROUND {round} STARTS\n\n')

                # Check if there are enough cards to start a new round
                try:
                    self.setup_round()
                except OutOfCards:
                    print("Out of cards!")
                    print(
                        f"\n\nFINAL WIN COUNT:\n\nDealer: {self.wins[self.dealer]}\nCounter: {self.wins[self.counter]}\nTies: {self.ties}")
                    break

                # Proceed with the game only if the deck setup was successful
                print("INITIAL HANDS")
                print("-------------")
                self.print_hands()

                # Check for blackjack status
                if (self.player_states[self.dealer] != "Blackjack" and
                        self.player_states[self.counter] != "Blackjack"):
                    self.play_round()

                self.score_round()
                print("FINAL HANDS")
                print("-----------")
                self.print_hands()

                # Reset for the next round
                for player in self.players:
                    player.clear_hand()
                    self.player_states[player] = "Playing"
                print(f'WIN COUNT: Dealer: {self.wins[self.dealer]}, Counter: {self.wins[self.counter]}\n\n')
                round += 1

        except OutOfCards:
            # Final catch for any unexpected out-of-cards situation
            print("Out of cards!")
            print(
                f"\n\nFINAL WIN COUNT:\n\nDealer: {self.wins[self.dealer]}\nCounter: {self.wins[self.counter]}\nTies: {self.ties}")

if __name__ == "__main__":
    blackjack = Blackjack()
    blackjack.run()