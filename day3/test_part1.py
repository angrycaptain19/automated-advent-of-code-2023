import pytest
from pathlib import Path
from .part1 import (
    find_symbols,
    find_numbers,
    is_adjacent_to_symbol,
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

def test_find_symbols(example_schematic):
    symbols = find_symbols(example_schematic)
    expected_symbols = {
        (3, 1),  # *
        (6, 3),  # #
        (3, 4),  # *
        (5, 5),  # +
        (3, 8),  # $
        (5, 8)   # *
    }
    assert symbols == expected_symbols

def test_find_numbers(example_schematic):
    numbers = find_numbers(example_schematic)
    expected = [
        (0, 2, 0, 467),
        (5, 7, 0, 114),
        (2, 3, 2, 35),
        (6, 8, 2, 633),
        (0, 2, 4, 617),
        (7, 8, 5, 58),
        (2, 4, 6, 592),
        (6, 8, 7, 755),
        (1, 3, 9, 664),
        (5, 7, 9, 598)
    ]
    assert numbers == expected

def test_is_adjacent_to_symbol():
    symbols = {(3, 1)}  # Just the * from the example
    # Test 467 which is adjacent to *
    assert is_adjacent_to_symbol((0, 2, 0, 467), symbols) == True
    # Test 114 which is not adjacent to any symbol
    assert is_adjacent_to_symbol((5, 7, 0, 114), symbols) == False

def test_process_schematic(example_schematic):
    result = process_schematic(example_schematic)
    assert result == 4361  # Sum of all valid part numbers from example

def test_empty_schematic():
    assert process_schematic([]) == 0

def test_single_line_schematic():
    assert process_schematic(["123"]) == 0  # No symbols, so no valid parts
    assert process_schematic(["123*"]) == 123  # Has symbol, so 123 is valid
