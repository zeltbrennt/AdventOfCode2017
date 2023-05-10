def part1(puzzle):
    x, y, _ = get_position(puzzle)
    return abs(x) + abs(y)

def part2(puzzle):
    return part1(puzzle)

def get_position(idx):
    x, y = (0, 0)
    state = 0
    num_steps = 1
    step = 1
    turn = 0
    while (step != idx):
        if state == 0: x += 1
        elif state == 1: y -= 1
        elif state == 2: x -= 1
        elif state == 3: y += 1
        if step % num_steps == 0: 
            state = (state + 1) % 4
            turn+= 1
            if turn % 2 == 0: num_steps+= 1
        step+= 1
    return (x, y, step & num_steps == 0)