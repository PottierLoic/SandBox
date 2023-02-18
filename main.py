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
    infoText = "Brush size : " + str(w.brush) + " | Material : " + str(w.selection)
    infoLabel.config(text=infoText)
    for y in range(len(w.grid)):
        for x in range(len(w.grid[y])):
            if w.grid[y][x] == 0:
                pass
            else:
                canvas.create_rectangle(x * CELL_SIZE, y * CELL_SIZE, x * CELL_SIZE + CELL_SIZE, y * CELL_SIZE + CELL_SIZE, fill=w.grid[y][x].color, outline=w.grid[y][x].color, tags=w.grid[y][x].type)

def update():
    if clickState == 1:
        w.add_cell(int(mousex/CELL_SIZE), int(mousey/CELL_SIZE))
    w.update()
    graphics()
    window.after(DELAY, update)

def click_press():
    global clickState
    clickState = 1

def click_release():
    global clickState
    clickState = 0

def motion(x, y):
    global mousex, mousey
    mousex, mousey = x, y

if __name__ == "__main__":
    # world inititalization 
    w = World() 
    clickState = 0
    mousex, mousey = 0, 0

    # Tkinter section.
    window = Tk()
    window.title("The sandbox")

    canvas = Canvas(window, bg=BACKGROUND_COLOR, height=GRID_HEIGHT*CELL_SIZE, width=GRID_WIDTH*CELL_SIZE)
    canvas.pack()
    
    infoText = "Brush size : " + str(w.brush) + " | Material : " + str(w.selection)
    infoLabel = Label(window, text=infoText)
    infoLabel.pack()

    window.update()

    # Bindings.
    window.bind("<ButtonPress-1>", lambda event: click_press())
    window.bind("<ButtonRelease-1>", lambda event: click_release())
    window.bind("<Motion>", lambda event: motion(event.x, event.y))
    window.bind("<Button-3>", lambda event: w.changeSelection())
    window.bind("<Up>", lambda event: w.changeBrush(1))
    window.bind("<Down>", lambda event: w.changeBrush(-1))

    # Main loop.
    update()

    window.mainloop()