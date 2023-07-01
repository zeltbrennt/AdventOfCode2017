from solutions import *

with open("input/day23.txt") as f:
    puzzle = f.read().splitlines()


print("\n\tDAY 23\n======================")
print(f"Part 1: {day23.part1(puzzle)}")
print(f"Part 2: {day23.part2(puzzle)}")

