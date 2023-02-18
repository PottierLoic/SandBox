"""
Bedrock material class
    Author : Loïc Pottier.
    Creation date : 16/02/2023.
"""

# Basic libraries
import random

# Local libraries.
from constants import *
from material import Material

class Bedrock(Material):
    """Bedrock class, inherit from the material abstract class"""

    def __init__(self) -> None:
        super().__init__("bedrock", "static")
        self.color = "pink"
        self.density = 100

    def nextState(self, around):
        """
        Modify attributes depending on material types around
        
            Returns:
                material (str): if the object need to transform.
                0: if he stay itself.
        """
        return 0