import re
from collections import Counter

def part1(puzzle: list[str]) -> str:
    for line in puzzle:
        name = line[:line.index(" ")]
        weight = int(re.findall("\d+", line)[0])
        program = Program(name, weight)
        if "->" in line:
            others = line[line.index(">")+2:].split(", ")
            program.placeholder_children(others)
        Program.all_Programs[name] = program
    # fix the placeholder
    for program in Program.all_Programs.values():
        for child in program.is_holding_up:
            idx = program.is_holding_up.index(child)
            program.is_holding_up[idx] = Program.all_Programs[child]
            Program.all_Programs[child].is_held_by = program
    for program in Program.all_Programs.values():
        if not program.is_held_by: return program.name

def part2(puzzle: list[str]):
    root = part1(puzzle)
    try: 
        Program.all_Programs[root].balance()
    except EarlyStop as solution:
        return int(str(solution))

class Program:
    all_Programs = {}
    def __init__(self, name: str, weight: int):
        self.name = name
        self.weight = weight
        self.is_holding_up = []
        self.is_held_by = None
        
    def __repr__(self) -> str:
        return f"{self.name} ({self.weight}) -> {self.is_holding_up}"
        
    def placeholder_children(self, names: list[str]) -> None:
        for name in names:
            self.is_holding_up.append(name)
            
    def balance(self) -> int:
        child_weights = []
        for child in self.is_holding_up:
            child_weights.append(child.balance())
        tally = Counter(child_weights)
        if len(tally) <= 1: 
            return self.weight + sum(child_weights)
        diff = tally.most_common()[0][0] - tally.most_common()[-1][0]
        unbalanced = child_weights.index(tally.most_common()[-1][0])
        answer = self.is_holding_up[unbalanced].weight + diff
        # return all the way to the top level 
        raise EarlyStop(answer)
    
class EarlyStop(Exception):
    pass