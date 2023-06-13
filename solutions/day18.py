
def part1(puzzle: list[str]):
    registry = {}
    idx = 0
    sound = None
    while True:
        instruction = puzzle[idx].split()
        if instruction[0] == "snd": 
            validate(instruction, registry)
            sound = registry.get(instruction[1])
        elif instruction[0] == "set":
            validate(instruction, registry)
            registry[instruction[1]] = execute(instruction, registry)
        elif instruction[0] == "add":
            validate(instruction, registry)
            registry[instruction[1]] += execute(instruction, registry)
        elif instruction[0] == "mul":
            validate(instruction, registry)
            registry[instruction[1]] *= execute(instruction, registry)
        elif instruction[0] == "mod":
            validate(instruction, registry)
            registry[instruction[1]] %= execute(instruction, registry)
        elif instruction[0] == "jgz":
            validate(instruction, registry)
            if (instruction[1].isdigit() and int(instruction[1]) > 0) or registry.get(instruction[1]) > 0:
                idx += int(instruction[2])
                continue
        elif instruction[0] == "rcv":
            validate(instruction, registry)
            if registry.get(instruction[1]) != 0: break
        idx += 1
        if idx >= len(puzzle): break
    return sound
    

def part2(puzzle):
    p0 = Program(0)
    p1 = Program(1)
    p0.partner = p1
    p1.partner = p0
    while not (p0.waiting and p1.waiting):
        p0.run(puzzle)
        p1.run(puzzle)
    return p1.counter
    

def execute(instruction: list[str], registry: dict[str, int]) -> int:
    return registry.get(instruction[2]) if instruction[2] in registry else int(instruction[2])

def validate(instruction: list[str], registry: dict[str, int]) -> None:
    if instruction[1] not in registry: registry[instruction[1]] = 0

class Program:
    def __init__(self, id: int) -> None:
        self.queue = []
        self.partner: Program = None
        self.waiting = False
        self.idx = 0
        self.registry = {'p': id}
        self.counter = 0
        
    def get_value(self, v: str) -> int:
        try:
            return int(v)
        except ValueError:
            return self.registry.get(v, 0)
        
    def run(self, code: list[str]):
        while not self.waiting:
            instruction = code[self.idx].split()
            if instruction[0] == "set":
                self.registry[instruction[1]] = self.get_value(instruction[2])
            elif instruction[0] == "add":
                self.registry[instruction[1]] += self.get_value(instruction[2])
            elif instruction[0] == "mul":
                self.registry[instruction[1]] *= self.get_value(instruction[2])
            elif instruction[0] == "mod":
                self.registry[instruction[1]] %= self.get_value(instruction[2])
            elif instruction[0] == "jgz":
                if self.get_value(instruction[1]) > 0:
                    self.idx += self.get_value(instruction[2])
                    continue
            elif instruction[0] == "snd": 
                value = self.get_value(instruction[1])
                self.partner.queue.append(value)
                self.partner.waiting = False
                self.counter += 1
            elif instruction[0] == "rcv":
                if self.queue:
                    self.registry[instruction[1]] = self.queue.pop(0)
                else:
                    self.waiting = True
                    break
            self.idx += 1