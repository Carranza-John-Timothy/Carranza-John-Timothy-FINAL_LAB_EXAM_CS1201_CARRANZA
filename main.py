import os
from utils.user_manager import UserManager
from utils.game_manager import GameManager
from utils.dice_game import DiceGame

user_file = 'users.txt'
game_file = 'games.txt'
user_manager = UserManager(user_file)
game_manager = GameManager(game_file)
dice_game = DiceGame()

def main():
    while True:
        try:            
            print("Welcome to Dice Roll Game!")
            print("1. Register")
            print("2. Login")
            print("3. Exit")

            choice = input("Enter your choice: ")

            if choice == '1':
                register()
            elif choice == "2":
                login()
            elif choice == "3":
                exit()
            else:
                print("Invalid Choice. Please Try again.")
        except ValueError:
            print("Invalid input. Please try again. ")

def register():
    while True: 
        username = input("Enter username (at least 4 characters) or leave blank to cancel: ")
        if not username:
            print("Register cancelled. ")
            return None 

        password = input("Enter password (at least 8 characters) or leave blank to cancel: ")

        if not password:
            print("Register cancelled.")
            return None

        if user_manager.register(username, password):
            print("Registration Successful!")
        else:
            print("Registration failed. Please try again.")

        main()

def login():
    while True:
            username = input("Enter username, or leave blank to cancel: ")

            if not username:
                print("Login cancelled. ")
                return None 

            password = input("Enter password, or leave blank to cancel: ")

            if not password:
                print("Login cancelled.")
                return None
                
            if user_manager.login(username, password):
                print(f"Welcome, {username}!")
                while True:
                    print("Logged in Menu:")
                    print("1. Start Game")
                    print("2. Show Top Scores")
                    print("3. Logout")
                    print("4. Exit")
                    choice = input("Enter your choice: ")
                    if choice == '1':
                        score = dice_game.play_game()
                        game_manager.save_game(username, score)
                    elif choice == '2':
                        top_scores = game_manager.get_top_scores(10)
                        for score in top_scores:
                            print(f"{score['username']}: {score['score']} ({score['datetime']})")
                    elif choice == '3':
                        break
                    elif choice == '4':
                        exit()
                    else:
                        print("Invalid choice. Please try again.")
            else:
                print("Invalid username or password. Please try again.")

if __name__ == '__main__':
    main()