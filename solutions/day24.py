
def part1(puzzle: list[str]) -> int:
    all_components = parse_input(puzzle)
    bridges = {}
    result = 0
    for comp in all_components:
        if 0 in comp:
            result = max(result, explore(comp, sorted([*comp]), all_components, [], bridges))
    od = dict(sorted(bridges.items(), reverse=True))
    return result
    

def part2(puzzle: list[str]) -> int:
    pass 

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
    bridges[sum(sum(x) for x in used_comp)] = used_comp
    return strength + sum(comp)

def get_next_comp(port: int, 
                used: list[list[int]], 
                all: list[list[int]]) -> list[list[int]]:
    next_comps = []
    for comp in all:
        if comp not in used and port in comp:
            next_comps.append(comp)
    return next_comps