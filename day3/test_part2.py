import pytest
from part2 import (
    find_gears,
    find_adjacent_numbers,
    process_schematic,
    find_numbers
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
    expected_gears = {(1, 3), (4, 3), (8, 5)}
    assert gears == expected_gears

def test_find_adjacent_numbers(example_schematic):
    numbers = find_numbers(example_schematic)
    gear_pos = (1, 3)  # First gear position
    adjacent_nums = find_adjacent_numbers(gear_pos, numbers, example_schematic)
    assert sorted(adjacent_nums) == [35, 467]

def test_process_schematic(example_schematic):
    result = process_schematic(example_schematic)
    assert result == 467835

def test_no_gears():
    schematic = [
        "123..456",
        "...$....",
        "789..012"
    ]
    assert process_schematic(schematic) == 0

def test_gear_with_single_number():
    schematic = [
        "123.....",
        "...*....",
        "........"
    ]
    assert process_schematic(schematic) == 0
