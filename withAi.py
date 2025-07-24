import random

# Valid moves
VALID_MOVES = ['rock', 'paper', 'scissors']

# Get player's move with input validation
def get_user_move():
    while True:
        move = input("Your move (rock/paper/scissors): ").lower().strip()
        if move in VALID_MOVES:
            return move
        print("❌ Invalid input. Please type 'rock', 'paper', or 'scissors'.")

# Random AI move
def get_ai_move():
    return random.choice(VALID_MOVES) #NOSONAR

# Determine winner
def get_winner(player, ai):
    if player == ai:
        return "tie"
    elif (
        (player == 'rock' and ai == 'scissors') or
        (player == 'paper' and ai == 'rock') or
        (player == 'scissors' and ai == 'paper')
    ):
        return "player"
    else:
        return "ai"

# Ask if player wants to play again (validated)
def ask_to_play_again():
    while True:
        choice = input("Play again? (y/n): ").lower().strip()
        if choice in ['y', 'n']:
            return choice == 'y'
        print("❌ Invalid input. Please enter 'y' or 'n'.")

# Display scoreboard
def print_scoreboard(score):
    print("\nScoreboard:")
    print(f"You     : {score['player']} wins")
    print(f"AI      : {score['ai']} wins")
    print(f"Ties    : {score['tie']} draws")
    print("-" * 25)

# Main game loop
def play_vs_ai():
    print("🎮 Welcome to Rock, Paper, Scissors — VS AI")

    # Initialize score
    score = {'player': 0, 'ai': 0, 'tie': 0}

    while True:
        # Get player and AI moves
        player_move = get_user_move()
        ai_move = get_ai_move()
        print(f"AI chose: {ai_move}")

        # Determine result
        result = get_winner(player_move, ai_move)
        if result == 'player':
            print("✅ You win!")
            score['player'] += 1
        elif result == 'ai':
            print("💻 AI wins!")
            score['ai'] += 1
        else:
            print("🤝 It's a tie!")
            score['tie'] += 1

        # Show scoreboard
        print_scoreboard(score)

        # Ask to play again
        if not ask_to_play_again():
            print("👋 Thanks for playing!")
            break

# Entry point
if __name__ == "__main__":
    play_vs_ai()
#done
