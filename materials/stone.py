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
        self.degradation = 0
        self.temperature = 0
        self.erosion = 0

    def nextState(self, around):
        """
        Modify attributes depending on material types around
        
            Returns:
                material (str): if the object need to transform.
                0: if he stay itself.
        """

        for type in around:
            if type == "acid":
                self.degradation += 1
            elif type == "lava":
                self.temperature += 1
            elif type == "water":
                self.erosion += 1

        if self.degradation >= STONE_ACID_RESISTANCE:
            return "destroy"        
        elif self.temperature >= STONE_TEMP_RESISTANCE:
            return "lava"
        elif self.erosion >= STONE_EROSION_RESISTANCE:
            return "sand"

        return 0