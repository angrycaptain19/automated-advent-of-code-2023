from pathlib import Path
from typing import List, Tuple, Set, Dict
from day3.part1 import find_numbers

def read_input(file_path: str) -> List[str]:
    with open(file_path) as f:
        return [line.strip() for line in f.readlines()]

def find_gears(schematic: List[str]) -> Set[Tuple[int, int]]:
    """Find all '*' symbols that could be gears."""
    gears = set()
    for i, line in enumerate(schematic):
        for j, char in enumerate(line):
            if char == '*':
                gears.add((i, j))
    return gears

def find_adjacent_numbers(gear_pos: Tuple[int, int], numbers: List[Tuple[int, int, int, int]], schematic: List[str]) -> List[int]:
    """Find all numbers adjacent to a gear position."""
    row, col = gear_pos
    adjacent = []
    
    for num_row, start_col, end_col, number in numbers:
        # Check if number is adjacent (including diagonally)
        if (abs(num_row - row) <= 1 and 
            any(abs(col - j) <= 1 for j in range(start_col, end_col))):
            adjacent.append(number)
    
    return adjacent

def calculate_gear_ratio(numbers: List[int]) -> int:
    """Calculate gear ratio if exactly two numbers are adjacent."""
    if len(numbers) == 2:
        return numbers[0] * numbers[1]
    return 0

def process_schematic(schematic: List[str]) -> int:
    """Find all gear ratios and sum them."""
    # Find all potential gears
    gears = find_gears(schematic)
    
    # Find all numbers in the schematic
    numbers = find_numbers(schematic)
    
    total = 0
    # For each gear, find adjacent numbers and calculate ratio
    for gear in gears:
        adjacent = find_adjacent_numbers(gear, numbers, schematic)
        total += calculate_gear_ratio(adjacent)
    
    return total

def main():
    input_path = Path(__file__).parent / "input.txt"
    schematic = read_input(str(input_path))
    result = process_schematic(schematic)
    print(f"Sum of gear ratios: {result}")

if __name__ == "__main__":
    main()
