#!/usr/bin/python

import sys
import snake
import random

from bolivianAnaconda import BolivianAnaconda
from congoWaterCobra import CongoWaterCobra

SNAKES = [
    BolivianAnaconda,
    CongoWaterCobra,
]

if sys.version.startswith('2'):
    # Import Tkinter, Python 2
    from Tkinter import *
    from ScrolledText import *
else:
    # Import tkinter, Python 3
    from tkinter import *
    from tkinter.scrolledtext import *

# Constants definition

# The size of one basic block on screen in pixel
BLOCK = 20 

class SnakeGame():
    def __init__(self, master, snakes, width=50, height=30):
        self.master = master
        self.width = width
        self.height = height
        self.canvas = Canvas(master, width=width*BLOCK, height=height*BLOCK)
        self.canvas.grid(row=0, column=0)
        self.field = snake.Field(self.canvas, width, height)
        y = height // 2 - 1
        x = (width - 2 * len(snakes)) // 2
        for s in snakes:
            self.field.add_snake(s(self.field, x, y, 0, random.choice([-1,1])))
            x += 2
        self.time = 0
        self.tick()

    def tick(self):
        if self.time % 10 == 0:
            self.field.new_mouse()
        for s in self.field.snakes:
            s.turn()
            s.move()
        self.time += 1
        self.canvas.after(50, self.tick)
        
# Main program

root = Tk()
root.title("Snakes")
app = SnakeGame(root, SNAKES)
root.mainloop()
