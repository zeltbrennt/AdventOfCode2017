from solutions import day10

def part1(puzzle):
    occupied = 0
    for i in range(128):
        seed = f"{puzzle}-{i}"
        hashvalue = day10.knot_hash(seed)
        for h in hashvalue:
            bits = int(h, 16).bit_count()
            occupied += bits
    return occupied

def part2(puzzle):
    grid = []
    for i in range(128):
        seed = f"{puzzle}-{i}"
        hashvalue = day10.knot_hash(seed)
        row = []
        for h in hashvalue:
            bit = list(format(int(h, 16),'0>4b'))
            row += bit
        grid.append(row)
    section = -1
    for i in range(128):
        for j in range(128):
            if explore(grid, i, j, section): section -= 1
    return (-section - 1)

def explore(grid, i, j, section):
    if isinstance(grid[i][j], str) and grid[i][j] in "01":
        grid[i][j] = section if grid[i][j] == "1" else "."
        if grid[i][j] == section: 
            for n_i, n_j in get_neighbors(i, j):
                explore(grid, n_i, n_j, section)
            return True
        return False
    return False
            
def get_neighbors(i, j):
    neighbors = []
    if i > 0 : neighbors.append((i-1, j))
    if i < 127: neighbors.append((i+1, j))
    if j > 0: neighbors.append((i, j-1))
    if j < 127: neighbors.append((i, j+1))
    return neighbors