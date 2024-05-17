import os
from utils.dice_game import DiceGame
from utils.game_manager import GameManager
from utils.user_manager import UserManager

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    user_file = 'users.txt'
    game_file = 'games.txt'

    user_manager = UserManager(user_file)
    game_manager = GameManager(game_file)

    while True:
        clear_screen()
        print("Welcome to the Dice Roll Game!")
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Please choose an option: ")

        if choice == '1':
            username = input("Enter username (at least 4 characters), or leave blank to cancel: ")
            if not username:
                continue
            password = input("Enter password (at least 8 characters), or leave blank to cancel: ")
            if not password:
                continue
            if user_manager.register(username, password):
                print("Registration successful!")
            else:
                print("Registration failed. Username might already be taken or invalid inputs.")
            input("Press Enter to continue...")
        elif choice == '2':
            username = input("Enter username, or leave blank to cancel: ")
            if not username:
                continue
            password = input("Enter password, or leave blank to cancel: ")
            if not password:
                continue
            if user_manager.login(username, password):
                clear_screen()
                print(f"Welcome, {username}!")
                while True:
                    print("Logged in Menu:")
                    print("1. Start Game")
                    print("2. Show Top Scores")
                    print("3. Logout")
                    print("4. Exit")
                    logged_in_choice = input("Please choose an option: ")

                    if logged_in_choice == '1':
                        dice_game = DiceGame()
                        score = dice_game.play_game()
                        if score > 0:
                            game_manager.save_game(username, score)
                        else:
                            print("You didn't win any stages. No record saved.")
                        input("Press Enter to continue...")
                    elif logged_in_choice == '2':
                        clear_screen()
                        top_scores = game_manager.get_top_scores()
                        if top_scores:
                            print("Top Scores:")
                            for i, game in enumerate(top_scores, start=1):
                                print(f"{i}. {game['username']} - {game['score']} points on {game['datetime']}")
                        else:
                            print("No scores to display yet.")
                        input("Press Enter to continue...")
                    elif logged_in_choice == '3':
                        break
                    elif logged_in_choice == '4':
                        print("Thank you for playing! Goodbye!")
                        exit()
                    else:
                        print("Invalid choice. Please try again.")
                        input("Press Enter to continue...")
            else:
                print("Login failed. Invalid username or password.")
                input("Press Enter to continue...")
        elif choice == '3':
            print("Thank you for playing! Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
            input("Press Enter to continue...")

if __name__ == "__main__":
    main()
