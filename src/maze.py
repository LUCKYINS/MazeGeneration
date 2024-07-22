"""
    Coder: Luckyyyin
"""
from random import randint
class Node:
    def __init__(self, up: bool= False, down: bool = False, left: bool = False, right: bool = False) -> None:
        self.up = up
        self.down = down
        self.left = left
        self.right = right
        self.position = None
        
    def addPosition(self, pos: tuple):
        self.position = pos
        
    def switchToTrue(self, value):
        match value:
            case 1:
                self.up = True
            case 2:
                self.down = True
            case 3:
                self.left = True
            case 4:
                self.right = True
        
    
class Grid:
    def __init__(self, width: int, height: int, division: int) -> None:
        self.width__ = width
        self.height__ = height
        self.division__ = division
        # Assure that the division is an int
        assert self.width__ % self.division__ == 0, "not int division"
        
    @property
    def width(self):
        return self.width__
    @property
    def height(self):
        return self.height__
    @property
    def dimension(self):
        return self.height * self.width
    @property
    def division(self):
        return self.division__

class Maze:
    def __init__(self, grid: Grid) -> None:
        #Number of node in a grid
        self.nodes: Node = [Node() for _ in range((((grid.width // grid.division) +1) **2))]
        self.createMaze(grid.width, grid.division)
        
    def createMaze(self, w:int, div):
        index = 0
        count = 0
        down = [(0, i) for i in range(w)]
        down.extend([(w, i) for i in range(0, w)])

        right = [(i, 0) for i in range(1, w)]
        right.extend([(i,w) for i in range(0, w-1)])
        for node in self.nodes:
            node.addPosition((index, count))
            if node.position !=(w, w) and node.position !=(w-1, w) and node.position not in down and node.position not in right:
                node.switchToTrue(randint(1, 4))
            if node.position in down:
                node.down = True
            if node.position in right:
                node.right = True
            index = index + div if index < w else 0
            count = count + div if index == 0 else count
            
    def checkValid(self, node: Node, nodes: list[Node]):
        pass


