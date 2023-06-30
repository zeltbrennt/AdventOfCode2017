from solutions import *

with open("input/day21.txt") as f:
    puzzle = f.read().splitlines()


print("\n\tDAY 21\n======================")
print(f"Part 1: {day21.part1(puzzle)}")
print(f"Part 2: {day21.part2(puzzle)}")
