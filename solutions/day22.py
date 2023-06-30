import numpy as np
import os
import time
from tqdm import tqdm

def part1(puzzle: list[str]):
    return solve(puzzle, 10000, 1)

def part2(puzzle: list[str]):
    return solve(puzzle, 10000000, 2)

def solve(puzzle: list[str], moves: int, ev: bool) -> int:
    virus = Virus(puzzle, ev)
    for _ in tqdm(range(moves)):
        virus.move()
#        virus.print()
    return virus.count()

class Virus:
    
    status = [' . ', ' W ', ' # ', ' F ']
    
    def __init__(self, repr: list[str], evolved = bool) -> None:
        self.evolved = evolved
        self.infection_counter = 0
        self.orientation = 0
        self.infected = {}
        repr = np.reshape([[*x] for x in repr], (len(repr), -1))
        map_x, map_y = repr.shape
        self.x = 0
        self.y = 0
        for iy, ix in np.ndindex(repr.shape):
            if repr[iy, ix] == '#':
                self.infected[(ix-map_x // 2,iy-map_y // 2)] = ' # '
                
    def count(self) -> None:
        return self.infection_counter
                
    def print(self) -> None:
        map = np.repeat(' . ', 72).reshape(8,9)
        map_x, map_y = map.shape
        for k, v in self.infected.items():
            x, y = k
            map[y + map_y // 2][x + map_x // 2] = v
        sy, sx = self.y+map_y // 2, self.x+map_x // 2
        if (self.x, self.y) in self.infected:
            map[sy][sx] = f"[{self.infected[(self.x, self.y)][1]}]"
        else: map[sy][sx] = f"[.]"
        for coord in map:
            print("".join(coord))
                    
    def move_simple(self) -> None:
        coord = (self.x, self.y)
        if coord in self.infected:
            self.orientation = (self.orientation + 1) % 4
            del self.infected[coord]
        else:
            self.orientation = (self.orientation - 1) % 4
            self.infected[coord] = ' # '
            self.infection_counter += 1
        if self.orientation == 0:
            self.y -= 1
        elif self.orientation == 1:
            self.x += 1
        elif self.orientation == 2:
            self.y += 1
        elif self.orientation == 3:
            self.x -= 1
            
    def move_complex(self) -> None:
        coord = (self.x, self.y)
        if coord not in self.infected or self.infected[coord] == ' . ':
            self.orientation = (self.orientation - 1) % 4
            self.infected[coord] = ' W '
        elif self.infected[coord] == ' W ':
            self.infected[coord] = ' # '
            self.infection_counter += 1
        elif self.infected[coord] == ' # ':
            self.infected[coord] = ' F '
            self.orientation = (self.orientation + 1) % 4
        elif self.infected[coord] == ' F ':
            self.infected[coord] = ' . '
            self.orientation = (self.orientation - 2) % 4
        if self.orientation == 0:
            self.y -= 1
        elif self.orientation == 1:
            self.x += 1
        elif self.orientation == 2:
            self.y += 1
        elif self.orientation == 3:
            self.x -= 1
    
    def move(self) -> None:
        if self.evolved: self.move_complex()
        else: self.move_simple()
        
