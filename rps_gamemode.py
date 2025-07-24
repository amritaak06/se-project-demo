import random

def get_player_choice(player_name):
    choices = ['rock', 'paper', 'scissors']
    choice = input(f"{player_name}, enter your move (rock/paper/scissors): ").lower()
    while choice not in choices:
        print("Invalid choice. Please try again.")
        choice = input(f"{player_name}, enter your move (rock/paper/scissors): ").lower()
    return choice

def determine_winner(choice1, choice2):
    if choice1 == choice2:
        return "It's a tie!"
    elif (choice1 == 'rock' and choice2 == 'scissors') or \
         (choice1 == 'paper' and choice2 == 'rock') or \
         (choice1 == 'scissors' and choice2 == 'paper'):
        return "Player 1 wins!"
    else:
        return "Player 2 wins!"

def two_player_mode():
    print("\n--- Two Player Mode ---")
    player1 = get_player_choice("Player 1")
    player2 = get_player_choice("Player 2")
    result = determine_winner(player1, player2)
    print(result)

def single_player_mode():
    print("\n--- Single Player vs AI Mode ---")
    player = get_player_choice("Player")
    ai = random.choice(CHOICES) #NOSONAR
    print(f"AI chose: {ai}")
    result = determine_winner(player, ai)
    print(result)

def main_menu():
    while True:
        print("\n====== Rock, Paper, Scissors ======")
        print("1. Play against another player")
        print("2. Play against the computer (AI)")
        print("3. Exit")

        choice = input("Choose a game mode (1-3): ")
        
        if choice == '1':
            two_player_mode()
        elif choice == '2':
            single_player_mode()
        elif choice == '3':
            print("Thanks for playing!")
            break
        else:
            print("Invalid selection. Please choose 1, 2, or 3.")

# rps_gamemode.py

def get_winner(player1, player2):
    beats = {"rock": "scissors", "scissors": "paper", "paper": "rock"}
    if player1 == player2:
        return "tie"
    elif beats[player1] == player2:
        return "player1"
    else:
        return "player2"


if __name__ == "__main__":
    main_menu()
