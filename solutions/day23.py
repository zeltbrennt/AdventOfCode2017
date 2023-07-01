
def part1(puzzle: list[str]):
    
    def get_value(v: str) -> int:
        try:
            return int(v)
        except ValueError:
            return registry.get(v, 0)

    registry = {'a':0, 'b':0, 'c':0, 'd':0,
                'e':0, 'f':0, 'g':0, 'h':0}
    idx = 0
    mul = 0
    while idx < len(puzzle): 
        do = puzzle[idx].split()
        if do[0] == "set":
            registry[do[1]] = get_value(do[2])
        elif do[0] == "sub":
            registry[do[1]] -= get_value(do[2])
        elif do[0] == "mul":
            registry[do[1]] *= get_value(do[2])
            mul += 1
        elif do[0] == "jnz":
            if get_value(do[1]) != 0:
                idx += get_value(do[2])
                continue
        idx += 1
    return mul

def part2(puzzle):
    pass

