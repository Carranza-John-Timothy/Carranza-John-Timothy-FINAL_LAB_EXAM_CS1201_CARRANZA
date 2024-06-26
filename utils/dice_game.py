import random

class DiceGame:
    def __init__(self):
        self.total_rounds = 3
        self.stage = 1
        self.score = 0
        self.stages_won = 0

    def play_round(self):
        while True:
            user_roll = random.randint(1, 6)
            computer_roll = random.randint(1, 6)
            print(f"Your roll: {user_roll}, Computer roll: {computer_roll}")
            if user_roll > computer_roll:
                return 1
            elif user_roll < computer_roll:
                return -1
            else:
                print("It's a tie. Rolling again...")

    def play_stage(self):
        wins = 0
        for _ in range(self.total_rounds):
            result = self.play_round()
            if result == 1:
                wins += 1
                print("You won this round!")
            elif result == -1:
                print("You lost this round.")
        if wins >= self.total_rounds // 2 + 1:
            self.score += 4
            self.stages_won += 1
            print("You won this stage!")
            return True
        else:
            print("You lost this stage. Game over.")
            return False

    def play_game(self):
        while True:
            if not self.play_stage():
                break
            self.stage += 1
            print(f"You have won {self.stage - 1} stages so far.")
            while True:
                response = input("Do you want to continue? (1/0): ")
                if response in ['1', '0']:
                    break
                print("Invalid input. Please enter 1 to continue or 0 to stop.")
            if response == '0':
                break
        print(f"Total points: {self.score}, Stages won: {self.stages_won}")
        return self.score
