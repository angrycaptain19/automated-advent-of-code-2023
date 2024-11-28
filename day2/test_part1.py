import pytest
from .part1 import parse_game_record, is_game_possible, sum_possible_game_ids

# Test data from the problem description
SAMPLE_GAMES = [
    "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
    "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
    "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
    "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
    "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"
]

def test_parse_game_record():
    game_id, cube_sets = parse_game_record(SAMPLE_GAMES[0])
    assert game_id == 1
    assert cube_sets == [
        {'blue': 3, 'red': 4, 'green': 0},
        {'red': 1, 'green': 2, 'blue': 6},
        {'green': 2, 'blue': 0, 'red': 0}
    ]

def test_is_game_possible():
    # Game 1 should be possible
    _, game1_sets = parse_game_record(SAMPLE_GAMES[0])
    assert is_game_possible(game1_sets) == True
    
    # Game 3 should be impossible (20 red)
    _, game3_sets = parse_game_record(SAMPLE_GAMES[2])
    assert is_game_possible(game3_sets) == False

def test_sum_possible_game_ids():
    # From example: games 1, 2, and 5 are possible (sum = 8)
    assert sum_possible_game_ids(SAMPLE_GAMES) == 8

def test_impossible_games():
    # Game 3 (too many red cubes)
    _, game3_sets = parse_game_record(SAMPLE_GAMES[2])
    assert is_game_possible(game3_sets) == False
    
    # Game 4 (too many blue cubes)
    _, game4_sets = parse_game_record(SAMPLE_GAMES[3])
    assert is_game_possible(game4_sets) == False
