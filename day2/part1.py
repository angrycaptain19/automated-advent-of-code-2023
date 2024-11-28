from typing import Dict, List, Tuple

# Game limits
RED_LIMIT = 12
GREEN_LIMIT = 13
BLUE_LIMIT = 14

def parse_game_record(line: str) -> Tuple[int, List[Dict[str, int]]]:
    """Parse a game record line into game ID and list of cube sets."""
    game_part, sets_part = line.split(': ')
    game_id = int(game_part.split(' ')[1])
    
    cube_sets = []
    for cube_set in sets_part.split('; '):
        cubes = {'red': 0, 'green': 0, 'blue': 0}
        for cube_count in cube_set.split(', '):
            count, color = cube_count.split(' ')
            cubes[color] = int(count)
        cube_sets.append(cubes)
    
    return game_id, cube_sets

def is_game_possible(cube_sets: List[Dict[str, int]]) -> bool:
    """Check if a game is possible given the cube limits."""
    for cube_set in cube_sets:
        if (cube_set.get('red', 0) > RED_LIMIT or
            cube_set.get('green', 0) > GREEN_LIMIT or
            cube_set.get('blue', 0) > BLUE_LIMIT):
            return False
    return True

def sum_possible_game_ids(games: List[str]) -> int:
    """Calculate sum of IDs for possible games."""
    total = 0
    for game in games:
        game_id, cube_sets = parse_game_record(game)
        if is_game_possible(cube_sets):
            total += game_id
    return total

def read_input(file_path: str) -> List[str]:
    """Read and return the puzzle input."""
    with open(file_path, 'r') as file:
        return [line.strip() for line in file if line.strip()]

def main():
    """Main function to solve the puzzle."""
    games = read_input('day2/input.txt')
    result = sum_possible_game_ids(games)
    print(f"Sum of possible game IDs: {result}")

if __name__ == '__main__':
    main()
