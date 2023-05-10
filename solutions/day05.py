
def part1(puzzle: list) -> int:
    ans, _ = jump(puzzle, False)
    return ans

def part2(puzzle):
    ans, _ = jump(puzzle, True)
    return ans

def jump(maze: list, part2: bool) -> tuple:
    idx = 0
    steps = 0
    while 0 <= idx < len(maze):
        offset = maze[idx]
        maze[idx] -= 1 if part2 and offset >=3 else -1 
        steps += 1
        idx += offset
    return steps, maze

