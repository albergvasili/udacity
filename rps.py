import random


class Player:

    def __init__(self):
        self.moves = ['rock', 'paper', 'scissors']
        self.count = 0
        self.their_move = ""
        self.my_move = ""

    def move(self, rounds):
        return 'rock'

    def learn(self, my_move, their_move):
        self.their_move = their_move
        self.my_move = my_move

    def beats(one, two):
        if one != two:
            return ((one == 'rock' and two == 'scissors') or
                    (one == 'scissors' and two == 'paper') or
                    (one == 'paper' and two == 'rock'))
        else:
            return 2


class RandomPlayer(Player):

    def move(self, rounds):
        return random.choice(self.moves)


class ReflectPlayer(Player):

    def move(self, rounds):
        if rounds == 1:
            return RandomPlayer.move(self, rounds)

        else:
            return self.their_move


class CyclePlayer(Player):

    def move(self, rounds):
        index = (rounds - 1) % 3

        if index == 0:
            random.shuffle(self.moves)
            return self.moves[index]

        else:
            return self.moves[index]


class HumanPlayer(Player):

    def move(self, rounds):
        self.moving = input("Rock, paper, scissors? > ").lower()

        for options in self.moves:  # Why?

            if self.moving in self.moves:
                return self.moving

            else:
                self.move(rounds)


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

        else:
            pass

        print("\tScore: " + str(self.p1.count) + " - " + str(self.p2.count)
              + "\n")

    def winner(self):
        if self.p1.count > self.p2.count:
            print("Player1 wins!")

        elif self.p1.count < self.p2.count:
            print("Player2 wins!")

        else:
            print("Tie")

    def play_round(self):
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
        print("Game start!")
        print(computer_player)
        for round in range(10):
            self.play_round()
        self.winner()
        print("Game over!")


if __name__ == '__main__':
    computer_classes = (Player(), RandomPlayer(), ReflectPlayer(), CyclePlayer())
    computer_player = random.choice(computer_classes)
    game = Game(HumanPlayer(), computer_player)
    game.play_game()
