import numpy as np
from tqdm import tqdm

def part1(puzzle):
    return solve(puzzle, 5)

def part2(puzzle):
    return solve(puzzle, 18)

def solve(puzzle: list[str], iter: int) -> int:
    picture = Pixels()
    for _ in tqdm(range(iter)):
        picture.divide()
        for line in puzzle:
            rule, newPattern = line.split(' => ')
            picture.apply(rule, newPattern)
        a, b, c, d = picture.nextIter.shape
        picture.pattern = picture.nextIter.swapaxes(1,2).reshape(a * c,b * d)
    return np.sum(picture.pattern == '#')

class Pixels:
    def __init__(self) -> None:
        self.pattern = np.reshape([*'.#./..#/###'.replace('/', '')], (3,3))
    
        
    def update(self, i, j, newPattern: str) -> None:
        pl = newPattern.count('/') + 1
        newPattern = np.reshape([*newPattern.replace('/', '')], (pl, pl))
        if (self.nextIter is None): self.nextIter = np.empty(self.divisions.shape[:2] + newPattern.shape, str)
        self.nextIter[i][j] = newPattern            
        
        
    def divide(self) -> None:
        h, w = self.pattern.shape
        if h % 2 == 0: div = 2
        else: div = 3
        self.divisions = self.pattern.reshape(h//div, div, -1, div).swapaxes(1,2)
        self.nextIter = None
        
    def apply(self, rule: str, newPattern: str) -> None:
        rl = rule.count('/') + 1
        rule = np.reshape([*rule.replace('/', '')], (rl,rl))
        for i, row in enumerate(self.divisions):
            for j, cell in enumerate(row):
                if cell.shape == rule.shape and np.sum(cell == '#') == np.sum(rule == '#'):
                    self.matchPattern(i, j, rule, cell, newPattern)
                
    def matchPattern(self, i, j, rule, cell, newPattern):
        for _ in range(4): 
            if np.array_equal(rule, cell):
                self.update(i, j, newPattern)
                return
            cell = np.rot90(cell) 
        cell = np.flip(cell, 0) 
        for _ in range(4):
            if np.array_equal(rule, cell):
                self.update(i, j, newPattern)
                return
            cell = np.rot90(cell)
        
    def print(self):
        for x in self.pattern:
            print(' '.join(x)) 
        print()
            