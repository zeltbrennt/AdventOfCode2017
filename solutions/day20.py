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
    particles = parse_input(puzzle)
    stop = 0
    while stop < 10:
        for p in particles:
            p.simulate_step()
        collisions = set()
        for i in range(len(particles)):
            for j in range(i + 1, len(particles)):
                if particles[i].pos == particles[j].pos:
                    collisions.add(particles[j].pos)
                    stop = 0
                    i += 1
                    j = i + 1
        particles = [p for p in particles if p.pos not in collisions]
        stop += 1
    return len(particles)
    

def parse_input(puzzle):
    particles = []
    for line in puzzle:
        coords =  [int(x) for x in re.split('\s+', re.sub('[^\d-]', ' ', line).strip())]
        particles.append(Particle(coords))
    return particles
        
        
        
class Particle:
    def __init__(self, params) -> None:
        self.pos = Vector(*params[0:3])
        self.vel = Vector(*params[3:6])
        self.acc = Vector(*params[6:9])
        
    def simulate_step(self):
        self.vel += self.acc
        self.pos += self.vel
    
    def __repr__(self) -> str:
        return f"p={self.pos}, v={self.vel}, a={self.acc}"
        
        
class Vector:
    def __init__(self, x, y, z) -> None:
        self.x = x
        self.y = y
        self.z = z
    
    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        z = self.z + other.z
        return Vector(x, y, z)
    
    def __eq__(self, __value: object) -> bool:
        return self.x == __value.x and self.y == __value.y and self.z == __value.z
    
    def __repr__(self) -> str:
        return f"<{self.x}, {self.y}, {self.z}>"
    
    def __hash__(self) -> int:
        return hash(self.__repr__())