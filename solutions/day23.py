import sympy

def part1(puzzle: list[str]):
    _, _, x = puzzle[0].split()
    return (int(x) - 2) ** 2

def part2(puzzle):
    _, _, x = puzzle[0].split()
    a = 100 * int(x) + 100000
    b = a + 17001
    return len([i for i in range(a, b, 17) if not sympy.isprime(i)])
