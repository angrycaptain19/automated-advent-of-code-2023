import pytest
from .part1 import extract_calibration_value, process_calibration_document

def test_extract_calibration_value():
    """Test extracting calibration values from individual lines."""
    assert extract_calibration_value("1abc2") == 12
    assert extract_calibration_value("pqr3stu8vwx") == 38
    assert extract_calibration_value("a1b2c3d4e5f") == 15
    assert extract_calibration_value("treb7uchet") == 77

def test_extract_calibration_value_invalid():
    """Test handling of invalid input lines."""
    with pytest.raises(ValueError):
        extract_calibration_value("abcdef")

def test_process_calibration_document():
    """Test processing the example from the problem description."""
    input_lines = [
        "1abc2",
        "pqr3stu8vwx",
        "a1b2c3d4e5f",
        "treb7uchet"
    ]
    assert process_calibration_document(input_lines) == 142

def test_process_calibration_document_empty():
    """Test processing empty document."""
    assert process_calibration_document([]) == 0
    assert process_calibration_document([""]) == 0
