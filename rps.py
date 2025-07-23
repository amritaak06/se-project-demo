# rock_paper_scissors_2p.py

# Step 1: Define possible moves
MOVES = ["rock", "paper", "scissors"]

# Step 2: Define the logic to determine the winner
def determine_winner(p1, p2):
    if p1 == p2:
        return "draw"
    elif (p1 == "rock" and p2 == "scissors") or \
         (p1 == "paper" and p2 == "rock") or \
         (p1 == "scissors" and p2 == "paper"):
        return "player1"
    else:
        return "player2"

# Step 3: Get a valid move from a player
def get_move(player_name):
    while True:
        move = input(f"{player_name}, enter your move (rock/paper/scissors): ").strip().lower()
        if move in MOVES:
            return move
        else:
            print("❌ Invalid move. Please choose rock, paper, or scissors.")

# Step 4: Main game loop
def main():
    print("🎮 Welcome to Rock-Paper-Scissors (2-Player Mode)")
    player1 = input("Enter Player 1's name: ").strip()
    player2 = input("Enter Player 2's name: ").strip()
    
    print("\n--- Round Begins ---\n")
    
    p1_move = get_move(player1)
    # Clear screen or add padding for fairness (optional)
    print("\n" * 50)
    p2_move = get_move(player2)

    result = determine_winner(p1_move, p2_move)

    print(f"\n📢 {player1} chose: {p1_move}")
    print(f"📢 {player2} chose: {p2_move}")

    if result == "draw":
        print("🤝 It's a draw!")
    elif result == "player1":
        print(f"🏆 {player1} wins!")
    else:
        print(f"🏆 {player2} wins!")

if __name__ == "__main__":
    main()
