"""
Stone material class
    Author : Loïc Pottier.
    Creation date : 16/02/2023.
"""

# Basic libraries
import random

# Local libraries.
from constants import *
from material import Material

class Stone(Material):
    """Stone class, inherit from the material abstract class"""

    def __init__(self) -> None:
        super().__init__("stone", "solid")
        self.color = random.choice(STONE_VARIATION)
        self.density = 3