from pathlib import Path
from typing import List, Tuple, Set, Dict
from collections import defaultdict

def read_input(file_path: str) -> List[str]:
    with open(file_path) as f:
        return [line.strip() for line in f.readlines()]

def find_numbers(schematic: List[str]) -> List[Tuple[int, int, int, int]]:
    numbers = []
    for row, line in enumerate(schematic):
        start_col = None
        current_num = ""
        
        for col, char in enumerate(line):
            if char.isdigit():
                if start_col is None:
                    start_col = col
                current_num += char
            elif start_col is not None:
                numbers.append((row, start_col, row, col - 1))
                start_col = None
                current_num = ""
                
        if start_col is not None:
            numbers.append((row, start_col, row, len(line) - 1))
            
    return numbers

def find_gears(schematic: List[str]) -> Set[Tuple[int, int]]:
    gears = set()
    for row, line in enumerate(schematic):
        for col, char in enumerate(line):
            if char == '*':
                gears.add((row, col))
    return gears

def get_number_at_position(schematic: List[str], pos: Tuple[int, int, int, int]) -> int:
    row, start_col, _, end_col = pos
    return int(schematic[row][start_col:end_col + 1])

def find_adjacent_numbers(gear_pos: Tuple[int, int], numbers: List[Tuple[int, int, int, int]], schematic: List[str]) -> List[int]:
    gear_row, gear_col = gear_pos
    adjacent_numbers = []
    
    for num_pos in numbers:
        row, start_col, _, end_col = num_pos
        # Check if number is adjacent (including diagonally)
        if (abs(row - gear_row) <= 1 and 
            any(abs(col - gear_col) <= 1 for col in range(start_col, end_col + 1))):
            adjacent_numbers.append(get_number_at_position(schematic, num_pos))
    
    return adjacent_numbers

def process_schematic(schematic: List[str]) -> int:
    gears = find_gears(schematic)
    numbers = find_numbers(schematic)
    total = 0
    
    for gear in gears:
        adjacent_nums = find_adjacent_numbers(gear, numbers, schematic)
        if len(adjacent_nums) == 2:
            total += adjacent_nums[0] * adjacent_nums[1]
            
    return total

def main():
    input_path = Path(__file__).parent / "input.txt"
    schematic = read_input(str(input_path))
    result = process_schematic(schematic)
    print(f"Sum of gear ratios: {result}")

if __name__ == "__main__":
    main()
