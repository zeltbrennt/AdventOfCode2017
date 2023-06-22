from solutions import *

with open("input/day19.txt") as f:
    puzzle = f.read().splitlines()
    

print("\n\tDAY 19\n======================")
print(f"Part 1: {day19.part1(puzzle)}")
print(f"Part 2: {day19.part2(puzzle)}")
