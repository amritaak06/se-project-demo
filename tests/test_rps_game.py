import pytest
from rps_gamemode import get_winner

# rps_gamemode.py

def get_winner(player, ai):
    beats = {"rock": "scissors", "scissors": "paper", "paper": "rock"}
    if player == ai:
        return "tie"
    elif beats[player] == ai:
        return "player"
    else:
        return "ai"

