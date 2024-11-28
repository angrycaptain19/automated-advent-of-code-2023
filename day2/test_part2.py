import pytest
from .part2 import (
    parse_game_record,
    find_minimum_cubes,
    calculate_power,
    sum_power_of_minimum_sets
)

@pytest.fixture
def sample_games():
    return [
        "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
        "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
        "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
        "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
        "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"
    ]

def test_find_minimum_cubes():
    _, cube_sets = parse_game_record("Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green")
    min_cubes = find_minimum_cubes(cube_sets)
    assert min_cubes == {'red': 4, 'green': 2, 'blue': 6}

def test_calculate_power():
    cube_set = {'red': 4, 'green': 2, 'blue': 6}
    assert calculate_power(cube_set) == 48

def test_sum_power_of_minimum_sets(sample_games):
    assert sum_power_of_minimum_sets(sample_games) == 2286

@pytest.mark.parametrize("game,expected_power", [
    ("Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green", 48),
    ("Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue", 12),
    ("Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red", 1560),
    ("Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red", 630),
    ("Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green", 36)
])
def test_individual_game_powers(game, expected_power):
    assert sum_power_of_minimum_sets([game]) == expected_power
