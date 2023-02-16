"""
Sandbox game.
    Author : Loïc Pottier.
    Creation date : 12/02/2023.
"""

# Basic library.
from tkinter import *

# Local library.
from constants import *
from world import World

def graphics():
    canvas.delete("cell")
    for y in range(len(w.grid)):
        for x in range(len(w.grid[y])):
            if w.grid[y][x] == 1:
                canvas.create_rectangle(x * CELL_SIZE, y * CELL_SIZE, x * CELL_SIZE + CELL_SIZE, y * CELL_SIZE + CELL_SIZE, fill="black", tags="cell")
   
def update():
    w.update()
    graphics()
    window.after(DELAY, update)

if __name__ == "__main__":
    # Tkinter section.
    window = Tk()
    window.title("The sandbox")

    canvas = Canvas(window, bg=BACKGROUND_COLOR, height=GRID_HEIGHT*CELL_SIZE, width=GRID_WIDTH*CELL_SIZE)
    canvas.pack()

    window.update()

    # Bindings.
    window.bind("<Button-1>", lambda event: w.add_cell(int(event.x/CELL_SIZE), int(event.y/CELL_SIZE), 1))

    # Main loop.
    w = World()
    update()

    window.mainloop()