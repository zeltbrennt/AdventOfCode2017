from tqdm import tqdm

def part1(puzzle):
    buffer = [0]
    position = 0
    for value in range(1, 2017 + 1):
        position = (position + puzzle + 1) % value
        buffer.insert(position + 1, value)
    return buffer[position + 2]


def part2(puzzle):
    position = 0
    ans = 0
    for value in range(1, 50_000_00 + 1):
        position = (position + puzzle + 1) % value
        if (position == 0): ans = value
    return ans
