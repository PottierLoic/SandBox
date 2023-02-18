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
        self.degradation = 0
        self.temperature = 0

    # def changeState(self, state):
    #     """
    #     Change the state of the material.

    #         Args:
    #             state (str): the state to change.
    #     """
    #     if state == "gas":
    #         self.type = "gas"
    #         self.state = "gas"
    #         self.color = random.choice(GAS_VARIATION)
    #         self.density = 0
    #     if state == "liquid":
    #         self.type = "water"
    #         self.state = "liquid"
    #         self.color = random.choice(WATER_VARIATION)
    #         self.density = 1

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
        
        if self.degradation >= WATER_ACID_RESISTANCE:
            return "acid"
        elif self.temperature >= WATER_TEMP_RESISTANCE:
            return "gas"
        return 0