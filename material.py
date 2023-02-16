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

    def nextPosition(self) -> tuple:
        """
        Determine the next position depending on the material state

            Returns:
                tuple (x, y): next position of the material
        """
        if self.state == None:  return (None)
        elif self.state == "gas":
            # do the gas comportement here
            pass
        elif self.state =="solid":
            # here check if solid can go under
            pass
        elif self.state == "liquid":
            # same as solid
            # but as liquid can flow on other materials, it need to check left/right once he can't go lower
            pass
        
    def nextState(self) -> str:
        """
        Determine the next state of the material

            Returns:
                newState (str): new state of the material
        """
        newState = None
        return newState
