"""
Material abstract class
    Author : Loïc Pottier.
    Creation date : 16/02/2023.
"""

# Local libraries.
from constants import *

class Material:
    """Abstract class representing a Material"""

    def __init__(self, type = None, state = None) -> None:
        """Initialise a blank material"""
        self.type = type
        self.state = state