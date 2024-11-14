import random

class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0

class Game:
    def __init__(self, player):
        self.player = player
        print("Welcome!\nDescription:\nYou have to guess if your number is higher or lower than the computer's number.")
    def play_round(self):
        user_num = random.randint(1, 100)
        comp_num = random.randint(1, 100)
        print("\nRound:")
        print(f"Your number: {user_num}")
        choice = input("Do you think your number is 'higher' or 'lower' than the computer's number?: ").strip().lower()
        print(f"Computer's number: {comp_num}")
        if choice == "higher":
            if user_num > comp_num:
                print("You win this round! Your guess was correct.")
                self.player.score += 1
            else:
                print("You lose this round. Your guess was incorrect.")
        elif choice == "lower":
            if user_num < comp_num:
                print("You win this round! Your guess was correct.")
                self.player.score += 1
            else:
                print("You lose this round. Your guess was incorrect.")
        else:
            print("Invalid choice. Please enter 'higher' or 'lower'.")
    def show_score(self):
        print(f"\n{self.player.name}'s current score: {self.player.score}")
player_name = input("Enter your name: ")
player = Player(player_name)
game = Game(player)
for round_num in range(1, 4):
    print(f"\nRound {round_num}")
    game.play_round()
    game.show_score()
print(f"\nFinal Score: {player.name} - {player.score}")
