from solutions import *

with open("input/day18.txt") as f:
    puzzle = f.read().splitlines()
    

print("\n\tDAY 18\n======================")
print(f"Part 1: {day18.part1(puzzle)}")
print(f"Part 2: {day18.part2(puzzle)}")
