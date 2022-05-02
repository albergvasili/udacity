"""Play rock paper scissors agains different computer player strategies."""
import random


class Player:
    """Base player superclass that always plays rock."""

    def __init__(self):
        """Define moves, counts, and variables to remember previous moves."""
        self.moves = ['rock', 'paper', 'scissors']
        self.count = 0
        self.their_move = ""
        self.my_move = ""

    def move(self, rounds):
        """Move rock."""
        return 'rock'

    def learn(self, my_move, their_move):
        """Remember moves."""
        self.their_move = their_move
        self.my_move = my_move

    def beats(one, two):
        """Return True if a player won the round."""
        if one != two:
            return ((one == 'rock' and two == 'scissors') or
                    (one == 'scissors' and two == 'paper') or
                    (one == 'paper' and two == 'rock'))
        else:
            return None


class RandomPlayer(Player):
    """Player class that picks moves randomly."""

    def move(self, rounds):
        """Chooose random move."""
        return random.choice(self.moves)


class ReflectPlayer(Player):
    """Player class that imitates the previous move of its opponent."""

    def move(self, rounds):
        """Start game by playing randomly, then imitate opponent's moves."""
        if rounds == 1:
            return RandomPlayer.move(self, rounds)

        else:
            return self.their_move


class CyclePlayer(Player):
    """Player class that cycles through possible moves."""

    def move(self, rounds):
        """Shuffle moves list for round 1, then cycle through moves."""
        index = (rounds - 1) % 3

        if index == 0:
            random.shuffle(self.moves)
            return self.moves[index]

        else:
            return self.moves[index]


class HumanPlayer(Player):
    """Player class for human."""

    def move(self, rounds):
        """Prompt message to make move, then return move or ask again."""
        moving = input("Rock, paper, scissors? > ").lower()

        if moving in self.moves:
            return moving

        else:
            move(rounds)


class Game:
    """Play game."""

    def __init__(self, p1, p2):
        """Define players and rounds."""
        self.p1 = p1
        self.p2 = p2
        self.round_count = 0

    def score_check(self, move1, move2):
        """Check moves and add points to the score."""
        score = Player.beats(move1, move2)

        if score == 1:
            self.p1.count += 1

        elif score == 0:
            self.p2.count += 1

        else:
            pass

        print("\tScore: " + str(self.p1.count) + " - " + str(self.p2.count)
              + "\n")

    def winner(self):
        """Check score to announce winner."""
        if self.p1.count > self.p2.count:
            print("Player1 wins!")

        elif self.p1.count < self.p2.count:
            print("Player2 wins!")

        else:
            print("Tie")

    def play_round(self):
        """Play a round."""
        self.round_count += 1
        rounds = self.round_count
        move1 = self.p1.move(rounds)
        move2 = self.p2.move(rounds)
        print(f"\nRound {rounds}:")
        print(f"Player1: {move1}\tPlayer2: {move2}")
        self.score_check(move1, move2)
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

    def play_game(self):
        """Start and end game."""
        print("\nGame start!")
        total_rounds = input("How many rounds would you like to play? > ")
        try:
            for round in range(int(total_rounds)):
                self.play_round()
            self.winner()
            print("\nGame over!")
        except ValueError:
            game.play_game()


if __name__ == '__main__':
    computer_classes = (Player(), RandomPlayer(), ReflectPlayer(),
                        CyclePlayer())
    computer_player = random.choice(computer_classes)
    game = Game(HumanPlayer(), computer_player)
    game.play_game()
