
def part1(puzzle: str) -> int:
    return walk(puzzle.split(","))[0]

def part2(puzzle: str) -> int:
    return walk(puzzle.split(","))[1]

def walk(route: str) -> tuple:
    x, y, z = (0, 0, 0)
    max_dist = 0
    for step in route:
        if step == "n": 
            z += 1
            y -= 1
        elif step == "ne": 
            x += 1
            y -= 1
        elif step == "se": 
            x += 1
            z -= 1
        elif step == "s": 
            y += 1
            z -= 1
        elif step == "sw": 
            y += 1
            x -= 1
        elif step == "nw": 
            z += 1
            x -= 1
        dist = max(abs(x), abs(y), abs(z))
        max_dist = max(dist, max_dist)
    return dist, max_dist