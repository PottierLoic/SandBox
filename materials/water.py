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

    def __init__(self, state) -> None:
        super().__init__("water", "liquid")
        self.degradation = 0
        if state == "liquid":
            self.color = random.choice(WATER_LIQUID_VARIATION)
            self.density = 1
            self.temperature = 20
        elif state == "solid":
            self.color = random.choice(WATER_SOLID_VARIATION)
            self.density = 4
            self.temperature = -5
        elif state == "gas":
            self.color = random.choice(WATER_GAS_VARIATION)
            self.density = 0
            self.temperature = 150

    def changeState(self, state):
        """
        Change the state of the material.

            Args:
                state (str): the state to change.
        """
        if state == "gas":
            self.state = "gas"
            self.color = random.choice(WATER_GAS_VARIATION)
            self.density = 0
        if state == "liquid":
            self.state = "liquid"
            self.color = random.choice(WATER_LIQUID_VARIATION)
            self.density = 1
        if state == "solid":
            self.state = "solid"
            self.color = random.choice(WATER_SOLID_VARIATION)
            self.density = 3

    def nextState(self, around):
        """
        Modify attributes depending on material types around
        
            Returns:
                material (str): if the object need to transform.
                0: if he stay itself.
        """

        if self.temperature < -5:
            self.temperature += 0.05
        elif self.temperature > 5:
            self.temperature -= 0.05


        for mat in around:
            if mat.type == "acid":
                self.degradation += 1
            elif mat.type == "stone" and mat.state == "liquid":
                self.temperature += 5
            elif mat.type == "bedrock":
                self.temperature -= 1
            elif mat.type == "water" and mat.state == "solid":
                self.temperature -= 0.2
        
        if self.degradation >= WATER_ACID_RESISTANCE:
            return "destroy"
        elif self.state != "gas" and self.temperature > WATER_EVAPORATION:
            self.changeState("gas")
        elif self.state != "solid" and self.temperature < WATER_SOLIDIFICATION:
            self.changeState("solid")
        elif self.state != "liquid" and self.temperature > WATER_SOLIDIFICATION and self.temperature < WATER_EVAPORATION:
            self.changeState("liquid")
        return 0