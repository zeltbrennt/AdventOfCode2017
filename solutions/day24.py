class Node:
        
    def __init__(self, repr: str) -> None:
        self.repr = repr
        self.ports = [int(x) for x in repr.split('/')]
        self.strength = sum(self.ports)

    def get_components(self, visited: list, all_nodes) -> list[str]:
        components = []
        for comp in all_nodes:
            if comp not in visited and self.ports[1] in comp.ports:
                if comp.ports.index(self.ports[1]) == 1: 
                    comp.flip()
                components.append(comp)
        return components
            
    def flip(self):
        self.ports = self.ports[::-1]
    
    def __str__(self) -> str:
        return f"{self.ports[0]}+{self.ports[1]}"
    
    def __repr__(self) -> str:
        return self.repr
    
    def __hash__(self) -> int:
        return hash(self.repr)
    

def part1(puzzle: list[str]) -> int:
    all_nodes = []
    for line in puzzle:
        all_nodes.append(Node(line))
    result = 0
    for node in all_nodes:
        if 0 in node.ports:
            temp = max(explore(node, [], all_nodes), result)
            result = max(result, temp)
    return result

def part2(puzzle):
    pass

def explore(node: Node, visited: list[Node], all_nodes: list[Node]):
    visited.append(node)
    strength = 0
    for n in node.get_components(visited, all_nodes):
        strength = max(strength, explore(n, visited.copy(), all_nodes))
    #print(" + ".join((str(x) for x in visited)),  "=", sum((x.strength for x in visited)))
    return strength + node.strength
        

    
    
#1591 low