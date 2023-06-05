def part1(puzzle: list[str]) -> int:
    return solve(puzzle, 1)
        
def part2(puzzle: list[str]) -> int:
    return solve(puzzle, 2)

def parse_instruction(registry: dict, line: str) -> int:
    tokens = line.split()
    reg = tokens[0]
    cond = tokens[4]
    if reg not in registry: registry[reg] = 0
    if cond not in registry: registry[cond] = 0
    tokens[0] = f"registry['{reg}']"
    tokens[4] = f"registry['{cond}']"
    tokens[1] = '-=' if tokens[1] == 'dec' else '+='
    instruction = ' '.join(tokens) + ' else 0'
    exec(instruction)
    return max(registry.values())

def solve(puzzle: list[str], part) -> int:
    registry = {}
    maximum = 0
    for line in puzzle:
        current = parse_instruction(registry, line)
        maximum = max(maximum, current)
    return current if part == 1 else maximum