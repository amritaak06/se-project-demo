import pytest
from rps_gamemode import determine_winner

@pytest.mark.parametrize("p1, p2, expected", [
    ('rock', 'scissors', "Player 1 wins!"),
    ('scissors', 'paper', "Player 1 wins!"),
    ('paper', 'rock', "Player 1 wins!"),
    ('scissors', 'rock', "Player 2 wins!"),
    ('paper', 'scissors', "Player 2 wins!"),
    ('rock', 'paper', "Player 2 wins!"),
    ('rock', 'rock', "It's a tie!"),
    ('paper', 'paper', "It's a tie!"),
    ('scissors', 'scissors', "It's a tie!"),
])
def test_determine_winner(p1, p2, expected):
    assert determine_winner(p1, p2) == expected
