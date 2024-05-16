import random

class DiceGame:
    def __init__(self):
        self.stage = 1
        self.score = 0

    def play_round(self):
        user_roll = random.randint(1, 6)
        computer_roll = random.randint(1, 6)
        print(f"Your roll: {user_roll}, Computer roll: {computer_roll}")
        if user_roll > computer_roll:
            return 1
        elif user_roll < computer_roll:
            return -1
        else:
            return 0

    def play_stage(self):
        wins = 0
        while True:
            result = self.play_round()
            if result == 1:
                wins += 1
                if wins == 3:
                    self.score += 4
                    print("You won this stage!")
                    return True
            elif result == -1:
                print("You lost this stage. Game over.")
                return False
            else:
                print("It's a tie. Let's play again.")

    def play_game(self):
        while True:
            if not self.play_stage():
                break
            self.stage += 1
            print(f"You have won {self.stage - 1} stages so far.")
            response = input("Do you want to continue? (1/0): ")
            if response == '0':
                break
        return self.score