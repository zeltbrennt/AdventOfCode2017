import re, math

def part1(puzzle: list[str]) -> int:
    for idx, line in enumerate(puzzle):
        coords =  [int(x) for x in re.split('\s+', re.sub('[^\d-]', ' ', line).strip())]
        pos = abs(coords[0] + abs(coords[1]) + abs(coords[2]))
        vel = math.sqrt(coords[3] ** 2 + coords[4] ** 2 + coords[5] ** 2)
        acc = math.sqrt(coords[6] ** 2 + coords[7] ** 2 + coords[8] ** 2)
        try:
            if acc < closest['acc']:
                closest = {'pos': pos, 'vel': vel, 'acc': acc, 'idx': idx}     
            elif acc == closest['acc']: 
                if vel < closest['vel']:
                    closest = {'pos': pos, 'vel': vel, 'acc': acc, 'idx': idx}
                elif vel == closest['vel']:
                    if pos < closest['pos']:
                        closest = {'pos': pos, 'vel': vel, 'acc': acc, 'idx': idx}
                        
        except:
            closest = {'pos': pos, 'vel': vel, 'acc': acc, 'idx': idx}
    return closest['idx']
            
        
def part2(puzzle):
    
    pass

def parse_input(puzzle):
    particles = []
    for line in puzzle:
        coords =  [int(x) for x in re.split('\s+', re.sub('[^\d-]', ' ', line).strip())]
        particles.append(Vector(coords))
    return particles
        
        
        
class Particle:
    def __init__(self, params) -> None:
        self.pos = Vector(params[0:3])
        self.vel = Vector(params[3:6])
        self.acc = Vector(params[6:9])
        
class Vector:
    def __init__(self, params) -> None:
        self.x = params[0]
        self.y = params[1]
        self.z = params[2]