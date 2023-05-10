from solutions import day04

with open("input/day04.txt") as f:
    puzzle = f.read().splitlines()

print(f"Part 1: {day04.part1(puzzle)}")
print(f"Part 2: {day04.part2(puzzle)}")