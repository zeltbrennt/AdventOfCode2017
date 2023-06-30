from solutions import *

with open("input/day22.txt") as f:
    puzzle = f.read().splitlines()


print("\n\tDAY 22\n======================")
print(f"Part 1: {day22.part1(puzzle)}")
print(f"Part 2: {day22.part2(puzzle)}")

