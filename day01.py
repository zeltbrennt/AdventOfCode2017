
def part1(puzzle):
    answer = int(puzzle[0]) if puzzle[0] == puzzle[-1] else 0
    prev = puzzle[0]
    for digit in puzzle[1:]:
        if digit == prev: answer += int(digit)
        prev = digit
    return answer

assert part1("1122") == 3
assert part1("1111") == 4
assert part1("1234") == 0
assert part1("91212129") == 9

print(f"Part1: {part1(puzzle)}")

def part2(puzzle):
    answer = 0
    offset = len(puzzle) // 2
    for i, d in enumerate(puzzle):
        if d == puzzle[(i + offset) % len(puzzle)]: answer += int(d)
    return answer

assert part2("1212") == 6
assert part2("1221") == 0
assert part2("123425") == 4
assert part2("123123") == 12
assert part2("12131415") == 4

print(f"Part2: {part2(puzzle)}")
