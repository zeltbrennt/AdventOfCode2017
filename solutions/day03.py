def part1(puzzle: int) -> int:
    x, y = (0, 0)
    state = 0
    num_steps = 1
    step = 1
    turn = 0
    while (step != puzzle):
        if state == 0: x += 1
        elif state == 1: y -= 1
        elif state == 2: x -= 1
        elif state == 3: y += 1
        if step % num_steps == 0: 
            state = (state + 1) % 4
            turn+= 1
            if turn % 2 == 0: num_steps+= 1
        step+= 1
    return abs(x) + abs(y)

def part2(puzzle: int) -> int:
    x, y = (0, 0)
    state = 0
    num_steps = 1
    step = 1
    turn = 0
    trace = {'0,0': 1}
    val = 0
    while (val <= puzzle):
        val = calc_value(trace,x, y)
        trace[f"{x},{y}"] = val
        if state == 0: x += 1
        elif state == 1: y -= 1
        elif state == 2: x -= 1
        elif state == 3: y += 1
        if step % num_steps == 0: 
            state = (state + 1) % 4
            turn+= 1
            if turn % 2 == 0: num_steps+= 1
        step+= 1
    return val

def calc_value(trace: dict, x: int, y: int) -> int:
    val = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            n = trace.get(f"{x+i},{y+j}")
            val += n if n else 0
    return val
