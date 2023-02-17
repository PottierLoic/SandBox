"""
Sandbox game.
    Author : Loïc Pottier.
    Creation date : 12/02/2023.
"""

# Basic libraries.
from tkinter import *

# Local libraries.
from constants import *
from world import World

def graphics():
    canvas.delete("all")
    for y in range(len(w.grid)):
        for x in range(len(w.grid[y])):
            if w.grid[y][x] == 0:
                pass
            else:
                canvas.create_rectangle(x * CELL_SIZE, y * CELL_SIZE, x * CELL_SIZE + CELL_SIZE, y * CELL_SIZE + CELL_SIZE, fill=w.grid[y][x].color, outline=w.grid[y][x].color, tags=w.grid[y][x].type)

def update():
    w.update()
    graphics()
    window.after(DELAY, update)

if __name__ == "__main__":
    # world inititalization 
    w = World() 

    # Tkinter section.
    window = Tk()
    window.title("The sandbox")

    canvas = Canvas(window, bg=BACKGROUND_COLOR, height=GRID_HEIGHT*CELL_SIZE, width=GRID_WIDTH*CELL_SIZE)
    canvas.pack()

    window.update()

    # Bindings.
    window.bind("<Button-1>", lambda event: w.add_cell(int(event.x/CELL_SIZE), int(event.y/CELL_SIZE)))
    window.bind("<Button-3>", lambda event: w.changeSelection())
    window.bind("<Up>", lambda event: w.changeBrush(1))
    window.bind("<Down>", lambda event: w.changeBrush(-1))

    # Main loop.
    update()

    window.mainloop()