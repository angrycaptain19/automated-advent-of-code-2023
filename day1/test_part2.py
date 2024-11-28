import pytest
from part2 import extract_calibration_value

def test_numeric_digits():
    assert extract_calibration_value("1abc2") == 12
    assert extract_calibration_value("pqr3stu8vwx") == 38

def test_spelled_out_numbers():
    assert extract_calibration_value("two1nine") == 29
    assert extract_calibration_value("eightwothree") == 83
    assert extract_calibration_value("abcone2threexyz") == 13
    assert extract_calibration_value("xtwone3four") == 24
    assert extract_calibration_value("4nineeightseven2") == 42
    assert extract_calibration_value("zoneight234") == 14
    assert extract_calibration_value("7pqrstsixteen") == 76

def test_overlapping_numbers():
    assert extract_calibration_value("oneight") == 18
    assert extract_calibration_value("twone") == 21
    assert extract_calibration_value("eightwo") == 82
    assert extract_calibration_value("nineight") == 98

def test_empty_input():
    assert extract_calibration_value("") == 0
    assert extract_calibration_value("abcdef") == 0

def test_single_digit():
    assert extract_calibration_value("1") == 11
    assert extract_calibration_value("two") == 22
