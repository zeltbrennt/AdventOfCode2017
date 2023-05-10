from solutions import *

with open("input/day07.txt") as f:
    puzzle = f.read().splitlines()

print("\n\tDAY 07\n======================")
print(f"Part 1: {day07.part1(puzzle)}")
print(f"Part 2: {day07.part2(puzzle)}")
