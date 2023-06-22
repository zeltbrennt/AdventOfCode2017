from tqdm import tqdm

def part1(puzzle: list[str]) -> str:
    programs = [chr(x) for x in range(97, 97+16)]
    return "".join(dance(programs, puzzle))
        
def part2(puzzle: list[str]) -> str:
    programs = [chr(x) for x in range(97, 97+16)]
    start = programs.copy()
    for i in range(1, 1_000_000_000):
        programs = dance(programs, puzzle)
        if programs == start: 
            for _ in range(1_000_000_000 % i):
                programs = dance(programs, puzzle)
            break
    return "".join(programs)

def spin(programs: list[str], size: int) -> list[str]:
        programs = programs[-size:] + programs[:-size]
        return programs
    
def exchange(programs: list[str], a: int, b: int) -> list[str]:
    programs[a], programs[b] = programs[b], programs[a]
    return programs

def partner(programs: list[str], a: str, b: str):
    return exchange(programs, programs.index(a), programs.index(b))

def dance(programs: list[str], moves: list[str]) -> list[str]:
    for move in moves:
        if move[0] == "s":
            programs = spin(programs, int(move[1:]))
        elif move[0] == "x":
            programs = exchange(programs, *(int(x) for x in move[1:].split("/")))
        elif move[0] == "p":
            programs = partner(programs, *move[1:].split("/"))
    return programs