from tqdm import tqdm

def part1(puzzle: tuple):
    return solve(40_000_000, *puzzle, 16807, 48271, 1, 1)
        
def part2(puzzle: tuple):
    return solve(5_000_000, *puzzle, 16807, 48271, 4, 8)

def generate(seed: int, mul: int, check: int) -> int:
    m = 2147483647
    while True:
        seed = (seed * mul) % m
        if seed % check == 0: return seed
        
def solve(rounds: int, a: int, b: int, mult_a: int, mult_b: int, check_a: int, check_b = int):
    total = 0
    for _ in tqdm(range(rounds), bar_format='{l_bar}{bar:20}{r_bar}{bar:-10b}'):
        a = generate(a, mult_a, check_a)
        b = generate(b, mult_b, check_b)
        if a & (1<<16) -1 == b & (1<<16) - 1: total += 1
    return total