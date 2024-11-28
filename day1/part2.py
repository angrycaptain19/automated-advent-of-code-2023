from .part1 import read_input

NUMBER_WORDS = {
    'one': '1', 'two': '2', 'three': '3', 'four': '4',
    'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'
}

def extract_calibration_value(line: str) -> int:
    """
    Extract calibration value from a line, considering both numeric digits
    and spelled-out numbers. Handles overlapping cases.
    """
    digits = []
    i = 0
    while i < len(line):
        # Check for numeric digit
        if line[i].isdigit():
            digits.append(line[i])
        else:
            # Check for spelled-out numbers
            for word, digit in NUMBER_WORDS.items():
                if line[i:].startswith(word):
                    digits.append(digit)
                    break
        i += 1
    
    if not digits:
        return 0
    
    return int(digits[0] + digits[-1])

def process_calibration_document(lines: list[str]) -> int:
    """
    Process all lines in the calibration document and return the sum of calibration values.
    """
    return sum(extract_calibration_value(line) for line in lines)

def main():
    lines = read_input('day1/input.txt')
    result = process_calibration_document(lines)
    print(f"Sum of calibration values: {result}")

if __name__ == '__main__':
    main()
