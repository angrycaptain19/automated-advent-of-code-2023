import pytest
from day4.part1 import parse_card, calculate_card_points, process_cards


def test_parse_card():
    line = "Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53"
    winning, player = parse_card(line)
    assert winning == {41, 48, 83, 86, 17}
    assert player == {83, 86, 6, 31, 17, 9, 48, 53}


def test_calculate_card_points():
    # Test case from example - Card 1 (4 matches = 8 points)
    winning = {41, 48, 83, 86, 17}
    player = {83, 86, 6, 31, 17, 9, 48, 53}
    assert calculate_card_points(winning, player) == 8

    # Test case with no matches
    winning = {1, 2, 3, 4, 5}
    player = {6, 7, 8, 9, 10}
    assert calculate_card_points(winning, player) == 0

    # Test case with one match (1 point)
    winning = {1, 2, 3, 4, 5}
    player = {1, 7, 8, 9, 10}
    assert calculate_card_points(winning, player) == 1

    # Test case with two matches (2 points)
    winning = {1, 2, 3, 4, 5}
    player = {1, 2, 8, 9, 10}
    assert calculate_card_points(winning, player) == 2


def test_process_cards():
    cards = [
        "Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53",
        "Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19",
        "Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1",
        "Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83",
        "Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36",
        "Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"
    ]
    assert process_cards(cards) == 13


def test_invalid_card_format():
    with pytest.raises(IndexError):
        parse_card("Invalid card format")
