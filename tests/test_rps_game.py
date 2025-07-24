import pytest
from rps_gamemode import get_winner

def test_get_winner_player_wins():
    assert get_winner('rock', 'scissors') == 'player'
    assert get_winner('paper', 'rock') == 'player'
    assert get_winner('scissors', 'paper') == 'player'

def test_get_winner_ai_wins():
    assert get_winner('scissors', 'rock') == 'ai'
    assert get_winner('rock', 'paper') == 'ai'
    assert get_winner('paper', 'scissors') == 'ai'

def test_get_winner_tie():
    assert get_winner('rock', 'rock') == 'tie'
    assert get_winner('paper', 'paper') == 'tie'
    assert get_winner('scissors', 'scissors') == 'tie'
