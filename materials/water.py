"""
Water material class.
    Author : Loïc Pottier.
    Creation date : 16/02/2023.
"""

# Basic libraries.
import random

# Local libraries.
from constants import *
from material import Material

class Water(Material):
    """Water class, inherit from the material abstract class"""

    def __init__(self) -> None:
        super().__init__("water", "liquid")
        self.color = random.choice(WATER_VARIATION)
        self.density = 1