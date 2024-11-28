def extract_calibration_value(line: str) -> int:
    """Extract the calibration value from a line by combining first and last digits."""
    # Find all digits in the line
    digits = [char for char in line if char.isdigit()]
    
    if not digits:
        raise ValueError(f"No digits found in line: {line}")
    
    # Combine first and last digits
    first_digit = digits[0]
    last_digit = digits[-1]
    return int(first_digit + last_digit)

def process_calibration_document(lines: list[str]) -> int:
    """Process all lines in the calibration document and return the sum of values."""
    total = 0
    for line in lines:
        if not line.strip():
            continue
        value = extract_calibration_value(line)
        total += value
    return total

def read_input(file_path: str) -> list[str]:
    """Read and return the contents of the input file."""
    try:
        with open(file_path, 'r') as f:
            return f.read().splitlines()
    except FileNotFoundError:
        raise FileNotFoundError(f"Input file not found: {file_path}")
    except Exception as e:
        raise Exception(f"Error reading input file: {str(e)}")

def main():
    """Main function to run the solution."""
    try:
        lines = read_input('day1/input.txt')
        result = process_calibration_document(lines)
        print(f"The sum of all calibration values is: {result}")
    except Exception as e:
        print(f"Error: {str(e)}")
        return 1
    return 0

if __name__ == '__main__':
    exit(main())
