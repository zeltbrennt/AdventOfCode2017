
def part1(puzzle):
    return solve(puzzle)[0]

def part2(puzzle):
    return solve(puzzle)[1]

def solve(input: str) -> int:
    score = 0
    total = 0
    garbage = False
    trash = 0
    char = 0
    while char < len(input):
        if garbage:
            if input[char] == "!": char += 1
            elif input[char] == ">": garbage = False
            else: trash += 1
        else:
            if input[char] == "{": score += 1
            elif input[char] == "}": 
                total += score
                score -= 1
            elif input[char] == "<": garbage = True
        char += 1
    return total, trash

