
def part1(puzzle: list[str]):
    firewall = {}
    severity = 0
    for line in puzzle:
        k, v = (int(x) for x in line.split(": "))
        firewall[k] = v
    total = k + 1
    for k, v in firewall.items():
        catch = [x for x in range(total) if x % (2 * v - 2) == 0]
        if k in catch: 
            severity += k * v
    return severity
    
def part2(puzzle):
    pass
