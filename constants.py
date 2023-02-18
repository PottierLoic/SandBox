"""
Constants module.
    Author : Loïc Pottier.
    Creation date : 12/02/2023.
"""

BACKGROUND_COLOR = "black" 
"""Basic color of the tkinter window"."""

CELL_SIZE = 18
"""Size of a cell side in pixels."""

GRID_HEIGHT = 40
"""Height of the world grid in cells."""

GRID_WIDTH = 60
"""Witdh of the world grid in cells."""

DELAY = 1
"""Delay between each world update in milliseconds."""

MATERIALS_LIST = ["stone", "sand", "water", "lava", "gas", "acid", "bedrock"]

STONE_VARIATION = ["#606060", "#737373", "#919191", "#757575"]
WATER_VARIATION = ["#1ca3ec", "#2389da", "#2389d1"]
LAVA_VARIATION = ["#ff321b", "#f1321d", "#ff4719"]
SAND_VARIATION = ["#FFFC83", "#FFFEBC", "#EFEA61"]
GAS_VARIATION = ["#D8D8D8", "#C8C8C8", "#B8B8B8"]
ACID_VARIATION = ["#00FF00", "#76FF76", "#3ADC3A"]

# STONE PROPERTIES
STONE_ACID_RESISTANCE = 50
STONE_TEMP_RESISTANCE = 50
STONE_EROSION_RESISTANCE = 200

# WATER PROPERTIES
WATER_ACID_RESISTANCE = 25
WATER_TEMP_RESISTANCE = 25

# LAVA PROPERTIES
LAVA_ACID_RESISTANCE = 25
LAVA_TEMP_RESISTANCE = 0

# SAND PROPERTIES
SAND_ACID_RESISTANCE = 25
SAND_TEMP_RESISTANCE = 25

#GAS PROPERTIES
GAS_TEMP_RESISTANCE = 0

#ACID PROPERTIES
ACID_TEMP_RESISTANCE = 25