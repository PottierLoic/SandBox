"""
Gas material class.
    Author : Loïc Pottier.
    Creation date : 16/02/2023.
"""

# Basic libraries.
import random

# Local libraries.
from constants import *
from material import Material

class Gas(Material):
    """Gas class, inherit from the material abstract class"""

    def __init__(self) -> None:
        super().__init__("gas", "gas")
        self.color = random.choice(GAS_VARIATION)
        self.density = 0
        self.temperature = 25

    def nextState(self, around):
        """
        Modify attributes depending on material types around
        
            Returns:
                material (str): if the object need to transform.
                0: if he stay itself.
        """
        for type in around:
            if type == "water":
                self.temperature -= 1

        self.temperature -= 0.1
        if self.temperature <= GAS_TEMP_RESISTANCE:
            return "water"
        return 0