
def part1(puzzle: list[str]) -> str:
    return solve(puzzle)[0]    

def part2(puzzle: list [str]) -> int:
    return solve(puzzle)[1]

def solve(puzzle: list[str]) -> tuple:
    x = puzzle[0].index('|')
    y = 0
    letters = []
    direction = 'd'
    counter = 0
    while True:
        counter += 1
        if direction == 'd': y += 1
        elif direction == 'u': y -= 1
        elif direction == 'r': x += 1
        elif direction == 'l': x -= 1
        step = puzzle[y][x]
        if step == ' ': return ''.join(letters), counter
        if step.isalpha(): letters.append(step)
        elif step == '+':
            if direction in 'du':
                if x >= 0 and puzzle[y][x-1] != ' ': direction = 'l'
                else: direction = 'r'
            else:
                if y >= 0 and puzzle[y-1][x] != ' ': direction = 'u'
                else: direction = 'd'            