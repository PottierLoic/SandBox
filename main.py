# Sandbox game
# Author : Loïc Pottier
# Date : 12/02/2023

# IMPORTS
from tkinter import *

# FILE IMPORTS
from constants import *
from game import Game

def graphics():
    canvas.delete("cell")
    for y in range(len(g.grid)):
        for x in range(len(g.grid[y])):
            if g.grid[y][x] == 1:
                canvas.create_rectangle(x * CELL_SIZE, y * CELL_SIZE, x * CELL_SIZE + CELL_SIZE, y * CELL_SIZE + CELL_SIZE, fill="black", tags="cell")
    window.after(DELAY, graphics)

if __name__ == "__main__":

    # TKINTER SECTION
    window = Tk()
    window.title("The sandbox game")

    canvas = Canvas(window, bg=BACKGROUND_COLOR, height=HEIGHT, width=WIDTH)
    canvas.pack()

    window.update()

    window.bind("<Button-1>", lambda event: g.add_cell(int(event.x/CELL_SIZE), int(event.y/CELL_SIZE), 1))

    # start
    g = Game()
    graphics()

    window.mainloop()