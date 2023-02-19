"""
Lava material class.
    Author : Loïc Pottier.
    Creation date : 16/02/2023.
"""

# Basic Libraries
import random

# Local libraries.
from constants import *
from material import Material

class Lava(Material):
    """Lava class, inherit from the material abstract class"""

    def __init__(self) -> None:
        super().__init__("lava", "liquid")
        self.color = random.choice(LAVA_VARIATION)
        self.density = 1
        self.temperature = 100

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
            elif type == "acid":
                self.temperature -= 1
            elif type == "stone":
                self.temperature -= 1
        self.temperature -= random.choice([0.05, 0.1, 0.01, 0.02])
        if self.temperature <= LAVA_TEMP_RESISTANCE:
            return "stone"

        return 0