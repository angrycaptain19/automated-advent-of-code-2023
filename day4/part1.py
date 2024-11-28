from pathlib import Path
from typing import List, Tuple, Set

def read_input(file_path: str) -> List[str]:
    """Read and return the input file contents as a list of strings."""
    return Path(file_path).read_text().splitlines()

def parse_card(line: str) -> Tuple[int, Set[int], Set[int]]:
    """Parse a card line and return card number, winning numbers, and player numbers."""
    card_part, numbers_part = line.split(':')
    card_number = int(card_part.split()[1])
    
    winning_part, player_part = numbers_part.split('|')
    winning_numbers = set(int(num) for num in winning_part.split())
    player_numbers = set(int(num) for num in player_part.split())
    
    return card_number, winning_numbers, player_numbers

def calculate_card_points(winning_numbers: Set[int], player_numbers: Set[int]) -> int:
    """Calculate points for a single card based on matching numbers."""
    matches = len(winning_numbers & player_numbers)
    if matches == 0:
        return 0
    return 1 << (matches - 1)  # 2^(matches-1)

def process_cards(cards: List[str]) -> int:
    """Process all cards and return total points."""
    total_points = 0
    for card in cards:
        _, winning_numbers, player_numbers = parse_card(card)
        points = calculate_card_points(winning_numbers, player_numbers)
        total_points += points
    return total_points

def main():
    """Main function to run the solution."""
    cards = read_input('day4/input.txt')
    result = process_cards(cards)
    print(f"Total points: {result}")

if __name__ == '__main__':
    main()
