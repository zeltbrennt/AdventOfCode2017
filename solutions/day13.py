
def part1(puzzle: list[str]) -> int:
    severity = 0
    for line in puzzle:
        d, r = (int(x) for x in line.split(": "))
        if d % (2 * r - 2) == 0: 
            severity += d * r
    return severity
    
def part2(puzzle: list[str]) -> int:
    delay = 0
    firewall = {}
    for line in puzzle:
        d, r = (int(x) for x in line.split(": "))
        firewall[d] = r
    catched = True
    while catched:
        catched = False
        for d, r in firewall.items():
            if (d + delay) % (2 * r - 2) == 0: 
                delay += 1
                catched = True
                break
    return delay
