from pathlib import Path
from typing import List, Set, Tuple, Dict

def read_input(file_path: str) -> List[str]:
    """Read and return the input file contents as a list of strings."""
    return Path(file_path).read_text().splitlines()

def find_symbols(schematic: List[str]) -> Set[Tuple[int, int]]:
    """Find all symbol positions (excluding periods) in the schematic."""
    symbols = set()
    for y, line in enumerate(schematic):
        for x, char in enumerate(line):
            if not char.isdigit() and char != '.':
                symbols.add((x, y))
    return symbols

def find_numbers(schematic: List[str]) -> List[Tuple[int, int, int, int]]:
    """Find all numbers and their positions in the schematic.
    Returns list of tuples (x_start, x_end, y, number)."""
    numbers = []
    for y, line in enumerate(schematic):
        x = 0
        while x < len(line):
            if line[x].isdigit():
                x_start = x
                num = ''
                while x < len(line) and line[x].isdigit():
                    num += line[x]
                    x += 1
                numbers.append((x_start, x - 1, y, int(num)))
            else:
                x += 1
    return numbers

def is_adjacent_to_symbol(number_pos: Tuple[int, int, int, int], symbols: Set[Tuple[int, int]]) -> bool:
    """Check if a number is adjacent to any symbol (including diagonally)."""
    x_start, x_end, y, _ = number_pos
    
    # Check all adjacent positions including diagonals
    for x in range(x_start - 1, x_end + 2):
        for y_offset in [-1, 0, 1]:
            if (x, y + y_offset) in symbols:
                return True
    return False

def process_schematic(schematic: List[str]) -> int:
    """Process the engine schematic and return the sum of all part numbers."""
    symbols = find_symbols(schematic)
    numbers = find_numbers(schematic)
    
    total = 0
    for number_pos in numbers:
        if is_adjacent_to_symbol(number_pos, symbols):
            total += number_pos[3]  # Add the number value
    
    return total

def main():
    """Main function to process the input and print the result."""
    input_path = Path(__file__).parent / "input.txt"
    schematic = read_input(str(input_path))
    result = process_schematic(schematic)
    print(f"The sum of all part numbers is: {result}")

if __name__ == "__main__":
    main()
