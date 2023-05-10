
def part1(puzzle: list) -> int:
    return len(list(filter(lambda x: isValid(x, 1), puzzle)))

def part2(puzzle: list) -> int:
    return len(list(filter(lambda x: isValid(x, 2), puzzle)))

def isValid(phrase: str, part: int) -> bool:
    if part == 1:
        phrase = phrase.split()
    elif part == 2:
        phrase = ["".join(sorted([*word])) for word in phrase.split()]
    return len(phrase) == len(set(phrase))
    