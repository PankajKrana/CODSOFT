import random

class RockPaperScissors:
    def __init__(self):
        self.options = ("rock", "paper", "scissors")
        self.running = True
        self.user_score = 0
        self.computer_score = 0

    def play_game(self):
        while self.running:
            player = None
            computer = random.choice(self.options)

            while player not in self.options:
                player = input("Enter a choice (rock, paper, scissors): ")

            print(f"Player: {player}")
            print(f"Computer: {computer}")

            if player == computer:
                print("It's a tie!")
            elif (player, computer) in (("rock", "scissors"), ("paper", "rock"), ("scissors", "paper")):
                print("You win!")
                self.user_score += 1
            else:
                print("You lose!")
                self.computer_score += 1

            print(f"Your score: {self.user_score}, Computer's score: {self.computer_score}")

            if not input("Play again? (y/n): ").lower() == "y":
                self.running = False

        print("Thanks for playing!")

game = RockPaperScissors()
game.play_game()
