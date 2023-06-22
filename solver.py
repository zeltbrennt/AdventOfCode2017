from solutions import *

with open("input/day20.txt") as f:
    puzzle = f.read().splitlines()
    

print("\n\tDAY 20\n======================")
print(f"Part 1: {day20.part1(puzzle)}")
print(f"Part 2: {day20.part2(puzzle)}")
