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

    def nextState(self, around):
        """
        Modify attributes depending on material types around
        
            Returns:
                material (str): if the object need to transform.
                0: if he stay itself.
        """
        for type in around:
            if type == "lava":
                return "gas"
        return 0