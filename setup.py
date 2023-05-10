boilerplate = """
def part1(puzzle):
    pass

def part2(puzzle):
    pass
"""   

for day in range(3, 26):
    file = f"solutions/day{str(day).zfill(2)}.py"
    f = open(file, "w")
    f.write(boilerplate)
    f.close()

