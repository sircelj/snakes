#!/usr/bin/python

# Glavni program. Deluje s Python 2.x in 3.x.

import sys
import snake
import random

### KONFIFGURACIJA KAC

# Svojo kaco dodate tako, da tu napisete ustrezni import

from bolivianAnaconda import BolivianAnaconda
from congoWaterCobra import CongoWaterCobra
from dwarfBoa import DwarfBoa
from kingCobra import KingCobra

# Nato v spisek SNAKES dodate razred, ki predstavlja vaso kaco

# Dodal sem nov komentar, ki ga bom hitro zbrisal

SNAKES = [
    BolivianAnaconda,
    CongoWaterCobra,
    DwarfBoa,
    KingCobra,
]

# Od tu naprej se ni treba nicesar dotikati

if sys.version.startswith('2'):
    # Import Tkinter, Python 2
    from Tkinter import *
    from ScrolledText import *
else:
    # Import tkinter, Python 3
    from tkinter import *
    from tkinter.scrolledtext import *

# Constants definition

class SnakeGame():
    """Razred, ki predstavlja celotno igrico."""
    def __init__(self, master, snakes, width=snake.WIDTH, height=snake.HEIGHT):
        self.master = master
        self.width = width
        self.height = height
        self.canvas = Canvas(master, width=width*snake.BLOCK, height=height*snake.BLOCK)
        self.canvas.grid(row=0, column=0)
        self.field = snake.Field(self.canvas, width, height)
        # postavimo kace v polje
        y = height // 2 - 1
        x = (width - 2 * len(snakes)) // 2
        random.shuffle(snakes)
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
        
# Glavni program
root = Tk()
root.title("Snakes")
app = SnakeGame(root, SNAKES)
root.mainloop()
