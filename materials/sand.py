"""
Sand class, inherit material properties, 
    Author : Loïc Pottier.
    Creation date : 16/02/2023.
"""

# Local libraries.
from constants import *
from material import Material

class Sand(Material):
    """Sand class, inherit from the material abstract class"""

    def __init__(self) -> None:
        super().__init__("sand", "solid")