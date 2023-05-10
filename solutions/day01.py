def part1(puzzle):
    answer = int(puzzle[0]) if puzzle[0] == puzzle[-1] else 0
    prev = puzzle[0]
    for digit in puzzle[1:]:
        if digit == prev: answer += int(digit)
        prev = digit
    return answer

def part2(puzzle):
    answer = 0
    offset = len(puzzle) // 2
    for i, d in enumerate(puzzle):
        if d == puzzle[(i + offset) % len(puzzle)]: answer += int(d)
    return answer
