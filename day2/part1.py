from typing import Dict, List, Tuple

# Constants for cube limits
RED_LIMIT = 12
GREEN_LIMIT = 13
BLUE_LIMIT = 14

def parse_game_record(line: str) -> Tuple[int, List[Dict[str, int]]]:
    """Parse a game record line into game ID and sets of cube counts."""
    game_part, sets_part = line.split(': ')
    game_id = int(game_part.split(' ')[1])
    
    sets = []
    for set_str in sets_part.split('; '):
        cube_counts = {'red': 0, 'green': 0, 'blue': 0}
        for cube_info in set_str.split(', '):
            count, color = cube_info.split(' ')
            cube_counts[color] = int(count)
        sets.append(cube_counts)
    
    return game_id, sets

def is_game_possible(sets: List[Dict[str, int]]) -> bool:
    """Check if a game is possible given the cube limits."""
    for set_counts in sets:
        if (set_counts.get('red', 0) > RED_LIMIT or
            set_counts.get('green', 0) > GREEN_LIMIT or
            set_counts.get('blue', 0) > BLUE_LIMIT):
            return False
    return True

def sum_possible_game_ids(game_records: List[str]) -> int:
    """Calculate the sum of IDs of possible games."""
    total = 0
    for record in game_records:
        game_id, sets = parse_game_record(record)
        if is_game_possible(sets):
            total += game_id
    return total

def read_input(file_path: str) -> List[str]:
    """Read and return the puzzle input file contents."""
    with open(file_path, 'r') as file:
        return file.read().splitlines()

def main():
    """Main function to solve the puzzle."""
    lines = read_input('day2/input.txt')
    result = sum_possible_game_ids(lines)
    print(f"Sum of possible game IDs: {result}")

if __name__ == '__main__':
    main()
