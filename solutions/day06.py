
def part1(puzzle):
    states = set()
    while str(puzzle) not in states:
        states.add(str(puzzle))
        balance(puzzle)
    return len(states)

def part2(puzzle):
    states = {}
    loop = 0
    while True:
        val = states.get(str(puzzle), 0)
        if val > 1: break
        if val == 1: loop += 1
        states[str(puzzle)] = val + 1
        balance(puzzle)
    return loop

def balance(memory: list) -> None:
    high = max(memory)
    bank = memory.index(high)
    memory[bank] = 0
    for _ in range(high):
        bank = (bank + 1) % len(memory)
        memory[bank] += 1
    return memory