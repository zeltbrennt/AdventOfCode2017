from solutions import *

with open("input/day05.txt") as f:
    puzzle = [int(x) for x in f.read().splitlines()]

print("\n\tDAY 05\n======================")
print(f"Part 1: {day05.part1(puzzle.copy())}")
print(f"Part 2: {day05.part2(puzzle.copy())}")
