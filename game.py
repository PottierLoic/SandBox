# game section
# Author : Loïc Pottier
# Date : 12/02/2023

# IMPORTS
import numpy as np

# FILE IMPORTS
from constants import *


class Game:
    def __init__(self) -> None:
        self.grid = np.zeros((HEIGHT, WIDTH), dtype=int)

    def update(self):
        pass

    def add_cell(self, x, y, cell_type):
        self.grid[y][x] = cell_type


    
