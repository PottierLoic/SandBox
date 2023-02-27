"""
Sandbox game.
    Author : Loïc Pottier.
    Creation date : 12/02/2023.
"""

# Basic libraries.
from tkinter import *
from PIL import Image, ImageTk
import time

# Local libraries.
from constants import *
from world import World

def graphics():
    canvas.delete("selection", "fps")
    infoText = "Brush size : " + str(w.brush) + " | Material : " + str(w.selection)
    infoLabel.config(text=infoText)
    # eraser and pencil button display
    canvas.create_image(25, 25, image=pencilImg, tags="interface")
    canvas.create_image(60, 25, image=eraserImg, tags="interface")
    if mode == 0:
        canvas.create_rectangle(12, 12, 38, 38, tags="selection")
    else:
        canvas.create_rectangle(47, 12, 73, 38, tags="selection")
    # materials display
    print(w)
    for y in range(len(w.grid)):
        for x in range(len(w.grid[y])):
            if w.grid[y][x] == w.oldGrid[y][x]:
                pass
            elif w.grid[y][x] == 0:
                print("supprime")
                canvas.delete(f'{x}, {y}')
            else:
                print("change")
                texte=f'{x}, {y}'
                canvas.delete(texte)
                canvas.create_rectangle(x*CELL_SIZE, y*CELL_SIZE, x*CELL_SIZE+CELL_SIZE, y*CELL_SIZE+CELL_SIZE, fill=w.grid[y][x].color, outline=w.grid[y][x].color, tags=texte)
    # Display fps
    canvas.create_text(GRID_WIDTH*CELL_SIZE - 60, GRID_HEIGHT*CELL_SIZE - 20, text=f"FPS: {round(frameRate)}", font="Arial 10", tag="fps")

def update():
    global prevTime, lastTime, frameRate
    if prevTime < PHYSICS_REFRESH_RATE:
        prevTime += time.time() - lastTime
    else:
        time1 = time.time()
        if clickState == 1:
            if mode == 0:
                w.add_cell(int(mousex/CELL_SIZE), int(mousey/CELL_SIZE))
            elif mode == 1:
                w.eraseCell(int(mousex/CELL_SIZE), int(mousey/CELL_SIZE))
        w.update()
        graphics()
        prevTime = 0
        time2 = time.time()
        try:
            frameRate = 1/(time2-time1)
        except ZeroDivisionError:
            pass
    lastTime = time.time()
    window.after(DELAY, update)

def click_press():
    global mode
    global clickState
    if 12<mousex<38 and 12<mousey<38:
        mode = 0
    elif 47<mousex<73 and 12<mousey<38:
        mode = 1
    else:
        clickState = 1

def click_release():
    global clickState
    clickState = 0

def motion(x, y):
    global mousex, mousey
    mousex, mousey = x, y

if __name__ == "__main__":
    # Variables.
    w = World() 
    clickState = 0
    mousex, mousey = 0, 0
    mode = 0

    frameRate = 10
    prevTime = 0
    lastTime = 0

    # Tkinter section.
    window = Tk()
    window.title("The sandbox")

    canvas = Canvas(window, bg=BACKGROUND_COLOR, height=GRID_HEIGHT*CELL_SIZE, width=GRID_WIDTH*CELL_SIZE)
    canvas.pack()
    
    infoText = "Brush size : " + str(w.brush) + " | Material : " + str(w.selection)
    infoLabel = Label(window, text=infoText)
    infoLabel.pack()

    window.update()

    pencilImg = ImageTk.PhotoImage(Image.open("img/pencil.png"))
    eraserImg = ImageTk.PhotoImage(Image.open("img/eraser.png"))

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