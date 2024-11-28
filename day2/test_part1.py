import pytest
from .part1 import parse_game_record, is_game_possible, sum_possible_game_ids

# Test data from the problem description
EXAMPLE_GAMES = [
    "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
    "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
    "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
    "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
    "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"
]

def test_parse_game_record():
    game_id, sets = parse_game_record(EXAMPLE_GAMES[0])
    assert game_id == 1
    assert sets == [
        {'blue': 3, 'red': 4, 'green': 0},
        {'red': 1, 'green': 2, 'blue': 6},
        {'green': 2, 'blue': 0, 'red': 0}
    ]

def test_is_game_possible():
    # Game 1 should be possible
    _, sets1 = parse_game_record(EXAMPLE_GAMES[0])
    assert is_game_possible(sets1) == True
    
    # Game 3 should be impossible (20 red)
    _, sets3 = parse_game_record(EXAMPLE_GAMES[2])
    assert is_game_possible(sets3) == False

def test_sum_possible_game_ids():
    # From example: games 1, 2, and 5 are possible (sum = 8)
    assert sum_possible_game_ids(EXAMPLE_GAMES) == 8

def test_parse_game_record_complex():
    game_id, sets = parse_game_record(EXAMPLE_GAMES[2])
    assert game_id == 3
    assert sets == [
        {'green': 8, 'blue': 6, 'red': 20},
        {'blue': 5, 'red': 4, 'green': 13},
        {'green': 5, 'red': 1, 'blue': 0}
    ]
