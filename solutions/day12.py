
def part1(puzzle: list[str]) -> int:
    connections = parse_input(puzzle) 
    return len(explore(connections, set(), '0'))

def part2(puzzle: list[str]) -> int:
    connections = parse_input(puzzle) 
    groups = 0
    for p in list(connections):
        if p in connections: 
            explore(connections, set(), p)
            groups += 1
    return groups

def parse_input(puzzle: list[str]) -> list:
    connections = {}
    for line in puzzle:
        p, con = line.split(" <-> ")
        con = con.split(", ")
        connections[p] = con
    return connections

def explore(maze: dict, visited: set, node: int) -> list:
    visited.add(node)
    for neighbor in maze[node]:
        if (neighbor not in visited): explore(maze, visited, neighbor)
    maze.pop(node)
    return visited