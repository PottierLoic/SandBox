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

    def __init__(self, state) -> None:
        super().__init__("stone", "solid")
        self.erosion = 0
        self.degradation = 0
        if state == "solid":
            self.color = random.choice(STONE_SOLID_VARIATION)
            self.density = 4
            self.temperature = 0
        elif state == "liquid":
            self.color = random.choice(STONE_LIQUID_VARIATION)
            self.density = 3
            self.temperature = 200

    def changeState(self, state):
        """
        Change the state of the material.

            Args:
                state (str): the state to change.
        """
        if state == "liquid":
            self.state = "liquid"
            self.color = random.choice(STONE_LIQUID_VARIATION)
            self.density = 3
            self.erosion == 0
            self.degradation == 0
        if state == "solid":
            self.state = "solid"
            self.color = random.choice(STONE_SOLID_VARIATION)
            self.density = 4

    def nextState(self, around):
        """
        Modify attributes depending on material types around
        
            Returns:
                material (str): if the object need to transform.
                0: if he stay itself.
        """

        for mat in around:
            if mat.type == "acid" and self.state == "solid":
                self.degradation += 1
            elif mat.type == "lava":
                self.temperature += 1
            elif mat.type == "water" and self.state == "solid":
                self.erosion += 1
                self.temperature -= 0.1
            elif mat.type == "water" and self.state == "liquid":
                self.temperature -= 0.1
            elif mat.type == "bedrock":
                self.temperature += 1

        if self.degradation > STONE_ACID_RESISTANCE:
            return "destroy"        
        elif self.state != "liquid" and self.temperature > STONE_TEMP_RESISTANCE:
            self.changeState("liquid")
        elif self.state != "solid" and self.temperature < STONE_TEMP_RESISTANCE:
            self.changeState("solid")
        elif self.erosion > STONE_EROSION_RESISTANCE:
            return "sand"
        
        return 0