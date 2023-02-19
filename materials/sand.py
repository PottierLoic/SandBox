"""
Sand class, inherit material properties, 
    Author : Loïc Pottier.
    Creation date : 16/02/2023.
"""

# Basic libraries
import random

# Local libraries.
from constants import *
from material import Material

class Sand(Material):
    """Sand class, inherit from the material abstract class"""

    def __init__(self) -> None:
        super().__init__("sand", "solid")
        self.color = random.choice(SAND_VARIATION)
        self.density = 4
        self.degradation = 0

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

        if self.degradation >= STONE_ACID_RESISTANCE:
            return "destroy"
        return 0