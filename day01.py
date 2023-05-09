

def part1(puzzle):
    answer = int(puzzle[0]) if puzzle[0] == puzzle[-1] else 0
    prev = puzzle[0]
    for digit in puzzle[1:]:
        if digit == prev: answer += int(digit)
        prev = digit
    return answer
    
print(f"Part1: {part1(puzzle)}")

