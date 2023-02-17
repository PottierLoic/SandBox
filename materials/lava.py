"""
Lava material class.
    Author : Loïc Pottier.
    Creation date : 16/02/2023.
"""

# Local libraries.
from constants import *
from material import Material

class Lava(Material):
    """Lava class, inherit from the material abstract class"""

    def __init__(self) -> None:
        super().__init__("lava", "liquid")
        self.color = "orange"
        self.density = 1