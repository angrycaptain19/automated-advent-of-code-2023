# Advent of Code Solutions

This repository contains solutions for the Advent of Code challenges.

## Day 1: Trebuchet?!

### Part 1: Calibration Values
Extracts calibration values from a document by combining first and last digits from each line.

To run the solution:
```bash
python -m day1.part1
```

To run tests:
```bash
pytest day1/test_part1.py -v
```

### Part 2: Spelled-Out Numbers
Enhances calibration value extraction to handle both numeric digits and spelled-out numbers (e.g., "one", "two", etc.).
Handles overlapping cases and combines first and last found digits.

To run the solution:
```bash
python -m day1.part2
```

To run tests:
```bash
pytest day1/test_part2.py -v
```

## Project Structure
```
.
└── day1/
    ├── __init__.py
    ├── part1.py
    ├── part2.py
    ├── test_part1.py
    ├── test_part2.py
    └── input.txt
```
