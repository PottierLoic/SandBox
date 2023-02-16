"""
World class.
    Author : Loïc Pottier.
    Creation date : 12/02/2023.
"""

# Basic libraries.
import numpy as np

# Local libraries.
from constants import *

class World:
    """Manage the world state and update materials in it."""

    def __init__(self) -> None:
        """Initialize the world."""
        self.grid = np.zeros((GRID_HEIGHT, GRID_WIDTH), dtype=int)

    def reset(self) -> None:
        """Reset the world."""
        self.__init__()

    def update(self) -> None:
        """Update every material of the grid."""
        pass

    def add_cell(self, x, y, mat) -> None:
        """
        Draw the given material on the grid.
        
            Parameters:
                x (int) : x index relative to cursor position.
                y (int) : y index relative to cursor position.
                mat (Material) : material type we want to draw.
        """

        len = int(BRUSH_SIZE/2)
        toDraw = []
        for dy in range(-len, len):
            for dx in range(-len, len):     
                toDraw.append([x+dx, y+dy])
        for coords in toDraw:
            if 0<coords[0]<len(self.grid[0]) and 0<coords[1]<len(self.grid) and self.grid[coords[1]][coords[0]] == 0:
                self.grid[coords[1]][coords[0]] = mat
