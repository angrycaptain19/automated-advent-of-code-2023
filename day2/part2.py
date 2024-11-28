from typing import Dict, List, Tuple

def parse_game_record(line: str) -> Tuple[int, List[Dict[str, int]]]:
    """Parse a game record line into game ID and list of cube sets"""
    game_part, sets_part = line.split(':')
    game_id = int(game_part.split()[1])
    
    cube_sets = []
    for cube_set in sets_part.split(';'):
        set_dict = {}
        for cube_count in cube_set.strip().split(','):
            count, color = cube_count.strip().split()
            set_dict[color] = int(count)
        cube_sets.append(set_dict)
    
    return game_id, cube_sets

def read_input(file_path: str) -> List[str]:
    with open(file_path, 'r') as file:
        return file.readlines()

def find_minimum_cubes(cube_sets: List[Dict[str, int]]) -> Dict[str, int]:
    """Find the minimum number of cubes needed for each color"""
    min_cubes = {'red': 0, 'green': 0, 'blue': 0}
    for cube_set in cube_sets:
        for color in min_cubes:
            if color in cube_set:
                min_cubes[color] = max(min_cubes[color], cube_set[color])
    return min_cubes

def calculate_power(cube_set: Dict[str, int]) -> int:
    """Calculate the power of a set of cubes (multiply the numbers together)"""
    return cube_set['red'] * cube_set['green'] * cube_set['blue']

def sum_power_of_minimum_sets(games: List[str]) -> int:
    """Calculate the sum of powers of minimum cube sets for all games"""
    total_power = 0
    for game in games:
        game_id, cube_sets = parse_game_record(game)
        min_cubes = find_minimum_cubes(cube_sets)
        total_power += calculate_power(min_cubes)
    return total_power

def main():
    games = read_input('day2/input.txt')
    result = sum_power_of_minimum_sets(games)
    print(f"Sum of powers of minimum cube sets: {result}")

if __name__ == '__main__':
    main()
