import pytest
from day3.part2 import (
    find_gears,
    find_adjacent_numbers,
    calculate_gear_ratio,
    process_schematic
)

@pytest.fixture
def example_schematic():
    return [
        "467..114..",
        "...*......",
        "..35..633.",
        "......#...",
        "617*......",
        ".....+.58.",
        "..592.....",
        "......755.",
        "...$.*....",
        ".664.598.."
    ]

def test_find_gears(example_schematic):
    gears = find_gears(example_schematic)
    expected = {(1, 3), (4, 3), (8, 5)}
    assert gears == expected

def test_calculate_gear_ratio():
    assert calculate_gear_ratio([467, 35]) == 16345
    assert calculate_gear_ratio([467]) == 0  # Not a gear - only one number
    assert calculate_gear_ratio([467, 35, 633]) == 0  # Not a gear - more than two numbers
    assert calculate_gear_ratio([]) == 0  # No numbers

def test_process_schematic(example_schematic):
    result = process_schematic(example_schematic)
    assert result == 467835
