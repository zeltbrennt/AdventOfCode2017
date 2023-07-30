def part1(puzzle: list[str]) -> int:
    global p1, p2
    p1, p2 = solve(puzzle)
    return p1

def solve(puzzle: list[str]) -> tuple: 
    all_components = parse_input(puzzle)
    bridges = {}
    result = 0
    for comp in all_components:
        if 0 in comp:
            result = max(result, explore(comp, sorted([*comp]), all_components, [], bridges)) # type: ignore
    return result, bridges
    

def part2(puzzle: list[str]) -> int:
    #p1, p2 = solve(puzzle)
    s = 0, 
    l = 0
    for k, v in p2.items():
        if len(v) == 30: print(k)
        if len(v) > l or (len(v) == l and k > s):
            s = k
            l = len(v)
    return s # type: ignore

def parse_input(input: list[str]) -> list[list[int]]:
    comp = []
    for line in input:
        comp.append([int(x) for x in line.split('/')])
    return comp

def explore(comp: list[int], 
            bridge: list[int], 
            all_comp: list[list[int]], 
            used_comp: list[list[int]],
            bridges: list[list[int]]):
    port = bridge[-1]
    used_comp.append(comp)
    strength = 0
    for c in get_next_comp(port, used_comp, all_comp):
        value = c[1 - c.index(port)]
        new_bridge = bridge + [value]
        strength = max(strength, explore(c, new_bridge, all_comp, used_comp.copy(), bridges))
    #print(used_comp, sum(sum(x) for x in used_comp))
    bridges[sum(sum(x) for x in used_comp)] = used_comp # type: ignore
    return strength + sum(comp)

def get_next_comp(port: int, 
                used: list[list[int]], 
                all: list[list[int]]) -> list[list[int]]:
    next_comps = []
    for comp in all:
        if comp not in used and port in comp:
            next_comps.append(comp)
    return next_comps