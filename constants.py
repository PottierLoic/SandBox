"""
Constants module.
    Author : Loïc Pottier.
    Creation date : 12/02/2023.
"""

BACKGROUND_COLOR = "white" 
"""Basic color of the tkinter window"."""

CELL_SIZE = 5
"""Size of a cell side in pixels."""

GRID_HEIGHT = 60
"""Height of the world grid in cells."""

GRID_WIDTH = 90
"""Witdh of the world grid in cells."""

DELAY = 1
"""Delay between each world update in milliseconds."""

MATERIALS_LIST = ["stone", "sand", "water", "ice", "lava", "acid", "bedrock", "gas"]
"""List of all drawable materials, used by the selection tool"""

PHYSICS_REFRESH_RATE = 1/120

# Color variation of each material
STONE_SOLID_VARIATION = ["#606060", "#737373", "#919191", "#757575"]
STONE_LIQUID_VARIATION = ["#ff321b", "#f1321d", "#ff4719"]
WATER_LIQUID_VARIATION = ["#1ca3ec", "#2389da", "#2389d1"]
WATER_GAS_VARIATION = ["#D8D8D8", "#C8C8C8", "#B8B8B8"]
WATER_SOLID_VARIATION = ["#66FFFF", "#67FFFF", "#66FFF0"]
SAND_VARIATION = ["#FFFC83", "#FFFEBC", "#EFEA61"]
ACID_VARIATION = ["#00FF00", "#76FF76", "#3ADC3A"]


# STONE PROPERTIES
STONE_ACID_RESISTANCE = 50
STONE_TEMP_RESISTANCE = 100
STONE_EROSION_RESISTANCE = 200

# WATER PROPERTIES
WATER_ACID_RESISTANCE = 25
WATER_EVAPORATION = 100
WATER_SOLIDIFICATION = 0

# SAND PROPERTIES
SAND_ACID_RESISTANCE = 25
SAND_TEMP_RESISTANCE = 25

#GAS PROPERTIES
GAS_TEMP_RESISTANCE = 0

#ACID PROPERTIES
ACID_TEMP_RESISTANCE = 25