import numpy as np
import os
import time

def part1(puzzle: list[str]):
    return solve(puzzle, 10000)

def part2(puzzle):
    pass

def solve(puzzle: list[str], moves: int) -> int:
    virus = Virus(puzzle)
    for _ in range(moves):
        virus.move()
    return virus.count()

class Virus:
    def __init__(self, repr: list[str]) -> None:
        self.infection_counter = 0
        self.orientation = 0
        self.infected = set()
        repr = np.reshape([[*x] for x in repr], (len(repr), -1))
        map_x, map_y = repr.shape
        self.x = 0
        self.y = 0
        for iy, ix in np.ndindex(repr.shape):
            if repr[iy, ix] == '#':
                self.infected.add(f"{ix-map_x // 2},{iy-map_y // 2}")
                
    def count(self) -> None:
        return self.infection_counter
                
    def print(self) -> None:
        map = np.repeat(' . ', 72).reshape(8,9)
        map_x, map_y = map.shape
        for i in self.infected:
            x, y = i.split(',')
            map[int(y) + map_y // 2][int(x) + map_x // 2] = ' # '
        if f"{self.x},{self.y}" in self.infected: virus = '[#]'
        else: virus = '[.]'
        map[self.y+map_y // 2][self.x+map_x // 2] = virus
        for coord in map:
            print("".join(coord))
                    
    def move(self) -> None:
        coord = f"{self.x},{self.y}"
        if coord in self.infected:
            self.orientation = (self.orientation + 1) % 4
            self.infected.remove(coord)
        else:
            self.orientation = (self.orientation - 1) % 4
            self.infected.add(coord)
            self.infection_counter += 1
        if self.orientation == 0:
            self.y -= 1
        elif self.orientation == 1:
            self.x += 1
        elif self.orientation == 2:
            self.y += 1
        elif self.orientation == 3:
            self.x -= 1
