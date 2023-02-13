# game section
# Author : Loïc Pottier
# Date : 12/02/2023

# IMPORTS
import numpy as np

# FILE IMPORTS
from constants import *

# contain the main grid and functions needed to draw on it
class Game:
    def __init__(self) -> None:
        self.grid = np.zeros((GRID_HEIGHT, GRID_WIDTH), dtype=int)

    #TODO: find the next state/position of all the cells
    # need to decide if all cells must find their next state themselve (by creating a new object for every cell)
    # or if everything must be checked here. prob better to do it separately
    def update(self):
        pass

    # draw the selected cell_type on the grid
    # only replace empty cells
    #TODO: modify it so it draw a round shape instead of a square
    def add_cell(self, x, y, cell_type):
        toDraw=[]
        for dy in range(-int(BRUSH_SIZE)/2, int(BRUSH_SIZE/2)):
            for dx in range(-int(BRUSH_SIZE)/2, int(BRUSH_SIZE/2)):
                toDraw.append([x+dx, y+dy])
        for coords in toDraw:
            if 0<coords[0]<len(self.grid[0]) and 0<coords[1]<len(self.grid) and self.grid[coords[1]][coords[0]]!=0:
                self.grid[y][x] = cell_type
    
    # return a printable string of the grid, used for debug purpose
    def __str__(self) -> str:
        s=""
        for row in self.grid:
            for value in row:
                s+=value+" "
            s+="\n"
        return s
