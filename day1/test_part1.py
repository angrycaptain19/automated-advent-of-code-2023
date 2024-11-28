import pytest
from .part1 import extract_calibration_value, process_calibration_document

def test_extract_calibration_value():
    """Test extracting calibration values from individual lines."""
    assert extract_calibration_value("1abc2") == 12
    assert extract_calibration_value("pqr3stu8vwx") == 38
    assert extract_calibration_value("a1b2c3d4e5f") == 15
    assert extract_calibration_value("treb7uchet") == 77

def test_extract_calibration_value_single_digit():
    """Test handling lines with only one digit."""
    assert extract_calibration_value("abc1def") == 11

def test_extract_calibration_value_error():
    """Test error handling for invalid input."""
    with pytest.raises(ValueError):
        extract_calibration_value("abcdef")

def test_process_calibration_document():
    """Test processing the example from the problem description."""
    test_input = [
        "1abc2",
        "pqr3stu8vwx",
        "a1b2c3d4e5f",
        "treb7uchet"
    ]
    assert process_calibration_document(test_input) == 142

def test_process_calibration_document_empty_lines():
    """Test handling empty lines in input."""
    test_input = [
        "1abc2",
        "",
        "pqr3stu8vwx",
        "   ",
        "treb7uchet"
    ]
    assert process_calibration_document(test_input) == 127
