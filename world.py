"""
World class.
    Author : Loïc Pottier.
    Creation date : 12/02/2023.
"""

# Basic libraries.
import numpy as np
import random
import copy

# Local libraries.
from constants import *
from materials.stone import *
from materials.sand import *
from materials.water import *
from materials.lava import *
from materials.gas import *

class World:
    """Manage the world state and update materials in it."""

    def __init__(self) -> None:
        """Initialize the world."""
        self.grid = np.zeros((GRID_HEIGHT, GRID_WIDTH), dtype=object)
        self.selection = "stone"
        self.checkState = 1
        self.brush = 3

    def reset(self) -> None:
        """Reset the world."""
        self.__init__()

    def update(self) -> None:
        """Update every material of the grid."""

        if self.checkState == 1:
            xStart, xEnd = 0, self.grid[0].size
        else:
            xStart, xEnd = self.grid[0].size-1, 0

        # Movement section.
        for y in range(len(self.grid)-1, 0, -1):
            for x in range(xStart, xEnd, self.checkState):
                if self.grid[y][x] == 0:
                    pass
                else:
                    newx, newy = self.getNextPosition(x, y)
                    if newx != x or newy != y:
                        temp = self.grid[newy][newx]
                        self.grid[newy][newx] = self.grid[y][x]
                        if temp == 0:
                            self.grid[y][x] = self.grid[y-1][x]
                            self.grid[y-1][x] = 0
                        else:
                            self.grid[y][x] = temp
        
        # State change section
        temp = copy.deepcopy(self.grid)
        for y in range(len(self.grid)-1, 0, -1):
            for x in range(xStart, xEnd, self.checkState):
                if self.grid[y][x] == 0:
                    pass
                else:
                    transform = self.grid[y][x].nextState(self.getMatAround(x, y))
                    if transform != 0:
                        if transform == "stone":
                            temp[y][x] = Stone()
                        elif transform == "sand":
                            temp[y][x] = Sand()
                        elif transform == "water":
                            temp[y][x] = Water()
                        elif transform == "lava":
                            temp[y][x] = Lava()
                        elif transform == "gas":
                            temp[y][x] = Gas()

        self.grid = temp

        self.checkState = -self.checkState

    def getMatAround(self, x, y) -> list:
        """
        Return a list of all the materials around x, y

            Parameters:
                x (int) : x position of the material in the grid.
                y (int) : y position of the material in the grid.

            Returns:
                around (list): type of materials found around. 
        """
        around = []
        if x-1>0 and self.grid[y][x-1]!=0:
            around.append(self.grid[y][x-1].type)
        if x+1<self.grid[0].size and self.grid[y][x+1]!=0:
            around.append(self.grid[y][x+1].type)
        if y-1>0 and self.grid[y-1][x]!=0:
            around.append(self.grid[y-1][x].type)
        if y+1<len(self.grid) and self.grid[y+1][x]!=0:
            around.append(self.grid[y+1][x].type)
        return around

    def getNextPosition(self, x, y) -> tuple:
        """
        Determine the next position of a material.

            Parameters:
                x (int) : x position of the material in the grid.
                y (int) : y position of the material in the grid.

            Returns:
                tuple (x, y): next position of the material.
        """
        if self.grid[y][x].state == None:  
            return (None)
        elif self.grid[y][x].state == "gas":
            # gas comportement here :
            # actually it doesn't move, need to add probability for him to move depending on its temperature
            # hot gas go up and cold gas go down, it could create nice flow
            return (x, y)
        elif self.grid[y][x].state =="solid":
            if self.canGoUnder(x, y):
                return (x, y+1)
            else:
                return (x, y)
        elif self.grid[y][x].state == "liquid":
            if self.canGoUnder(x, y):
                return (x, y+1)
            else:
                direction = self.canFlow(x, y)
                if direction == "l": return (x-1, y)
                elif direction == "r": return (x+1, y)
                elif direction == "lr":
                    if random.randrange(2) == 0: 
                        return (x-1, y)
                    else: return (x+1, y)
                else: return (x, y)

    def canFlow(self, x, y) -> str:
        """
        Return the direction where the liquid can go.
        
            Parameters:
                x (int) : x position of the material in the grid.
                y (int) : y position of the material in the grid.

            Returns:
                "l" if it can only go left. 
                "r" if it can only go right. 
                "lr" if it can go to both sides.
                "no" if it can't move
        """
        left = True
        right = True
        if x-1 < 0:
            left = False
        elif self.grid[y][x-1] != 0 :
            if self.grid[y][x-1].density < self.grid[y][x].density:
                left = True
            else:
                left = False
        if x+1 >= self.grid[0].size:
            right = False
        elif self.grid[y][x+1] != 0 :
            if self.grid[y][x+1].density < self.grid[y][x].density:
                right = True
            else:
                right = False
        
        if left and right: return "lr"
        elif left and not right: return "l"
        elif not left and right: return "r"
        else: return ""

    def canGoUnder(self, x, y) -> bool:
        """
        Return true if the material provided can go down by 1.
        
            Parameters:
                x (int) : x position of the material in the grid.
                y (int) : y position of the material in the grid.

            Returns:
                True if it can go down, False if there is already something, or out of bound.
        """
        if y+1 >= len(self.grid):
            return False
        elif self.grid[y+1][x]!=0:
            if self.grid[y+1][x].density < self.grid[y][x].density:
                return True
        else: 
            return True

    def changeSelection(self) -> None:
        """Switch to the next material"""
        ind = MATERIALS_LIST.index(self.selection)
        self.selection = MATERIALS_LIST[(ind+1)%(len(MATERIALS_LIST))]
        print(self.selection)

    def changeBrush(self, incr) -> None:
        """Change the brush size depending on incr value"""
        if incr == -1 and self.brush > 3 or incr == 1:
            self.brush += incr
        print(self.brush)

    def add_cell(self, x, y) -> None:
        """
        Draw the selected material on the grid.
        
            Parameters:
                x (int) : x grid index relative to cursor position.
                y (int) : y grid index relative to cursor position.
        """
        len = int(self.brush/2)
        toDraw = []
        for dy in range(-len, len):     
            for dx in range(-len, len):     
                toDraw.append((x+dx, y+dy))
        for coords in toDraw:
            if 0<=coords[0]<=self.grid[0].size and 0<=coords[1]<=self.grid.size and self.grid[coords[1]][coords[0]] == 0:
                if self.selection == "stone":
                    self.grid[coords[1]][coords[0]] = Stone()
                elif self.selection == "sand":
                    self.grid[coords[1]][coords[0]] = Sand()
                elif self.selection == "water":
                    self.grid[coords[1]][coords[0]] = Water()
                elif self.selection == "lava":
                    self.grid[coords[1]][coords[0]] = Lava()
                elif self.selection == "gas":
                    self.grid[coords[1]][coords[0]] = Gas()


