
def part1(puzzle: list[str]):
    registry = {}
    idx = 0
    sound = None
    while True:
        instruction = puzzle[idx].split()
        if instruction[0] == "snd": 
            validate(instruction, registry)
            sound = registry.get(instruction[1])
        elif instruction[0] == "set":
            validate(instruction, registry)
            registry[instruction[1]] = execute(instruction, registry)
        elif instruction[0] == "add":
            validate(instruction, registry)
            registry[instruction[1]] += execute(instruction, registry)
        elif instruction[0] == "mul":
            validate(instruction, registry)
            registry[instruction[1]] *= execute(instruction, registry)
        elif instruction[0] == "mod":
            validate(instruction, registry)
            registry[instruction[1]] %= execute(instruction, registry)
        elif instruction[0] == "jgz":
            validate(instruction, registry)
            if (instruction[1].isdigit() and int(instruction[1]) > 0) or registry.get(instruction[1]) > 0:
                idx += int(instruction[2])
                continue
        elif instruction[0] == "rcv":
            validate(instruction, registry)
            if registry.get(instruction[1]) != 0: break
        idx += 1
        if idx >= len(puzzle): break
    return sound
            
def part2(puzzle):
    pass

def execute(instruction: list[str], registry: dict[str, int]) -> int:
    return registry.get(instruction[2]) if instruction[2] in registry else int(instruction[2])

def validate(instruction: list[str], registry: dict[str, int]) -> None:
    if instruction[1] not in registry: registry[instruction[1]] = 0