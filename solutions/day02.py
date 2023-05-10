def part1(puzzle: list) -> int:
    answer = 0
    for row in puzzle:
        minimum = float('inf')
        maximum = float('-inf')
        for digit in row:
            minimum = min(minimum, digit)
            maximum = max(maximum, digit)
        answer += maximum - minimum
    return answer

def part2(puzzle: list) -> int:
    answer = 0
    for row in puzzle:
        for a in range(len(row)):
            for b in range(a+1, len(row)):
                if row[a] % row[b] == 0:
                    answer += row[a] // row[b]
                elif row[b] % row[a] == 0: 
                    answer += row[b] // row[a]
    return answer
