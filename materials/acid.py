"""
Acid material class.
    Author : Loïc Pottier.
    Creation date : 16/02/2023.
"""

# Basic Libraries
import random

# Local libraries.
from constants import *
from material import Material

class Acid(Material):
    """Acid class, inherit from the material abstract class"""

    def __init__(self) -> None:
        super().__init__("acid", "liquid")
        self.color = random.choice(ACID_VARIATION)
        self.density = 1
        self.temperature = 0

    def nextState(self, around):
        """
        Modify attributes depending on material types around
        
            Returns:
                material (str): if the object need to transform.
                0: if he stay itself.
        """
        for type in around:
            if type == "lava":
                self.temperature += 1

        if self.temperature >= ACID_TEMP_RESISTANCE:
            return "gas"
        return 0