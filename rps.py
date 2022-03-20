import random
moves = ['rock', 'paper', 'scissors']


class Player:

    def __init__(self):
        self.count = 0

    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        pass

    def beats(one, two):
        return ((one == 'rock' and two == 'scissors') or
                (one == 'scissors' and two == 'paper') or
                (one == 'paper' and two == 'rock'))


class RandomPlayer(Player):

    def move(self):
        return random.choice(moves)


class HumanPlayer(Player):

    def move(self):
        self.moving = input("Rock, paper, scissors? > ").lower()

        for options in moves:  # Why?

            if self.moving in moves:
                return self.moving

            else:
                self.move()


class Game:

    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.round_count = 0

    def score_check(self, move1, move2):
        score = Player.beats(move1, move2)

        if score == 1:
            self.p1.count += 1

        elif score == 0:
            self.p2.count += 1

        print("\tScore: " + str(self.p1.count) + " - " + str(self.p2.count)
              + "\n")

    def winner(self):
        if self.p1.count >= self.p2.count:
            print("Player1 wins!") 

        elif self.p1.count <= self.p2.count:
            print("Player2 wins!")

        else:
            print("Tie")

    def play_round(self):
        self.round_count += 1
        rounds = self.round_count
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"\nRound {rounds}:")
        print(f"Player1: {move1}\tPlayer2: {move2}")
        self.score_check(move1, move2)
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

    def play_game(self):
        print("Game start!")
        for round in range(3):
            self.play_round()
        self.winner()
        print("Game over!")


if __name__ == '__main__':
    game = Game(HumanPlayer(), RandomPlayer())
    game.play_game()
