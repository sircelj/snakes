#!/usr/bin/python

from Tkinter import *
import random

BLOCK = 20

UP    = 0
LEFT  = 1
DOWN  = 2
RIGHT = 3
direction = [(0,-1), (-1,0), (0,1), (1,0)]

def left(d):
    return (d + 3) % 4

def right(d):
    return (d + 1) % 4

class Wall():
    def __init__(self, canvas, x, y):
        self.x = BLOCK * x
        self.y = BLOCK * y
        self.widget = canvas.create_rectangle(self.x+2, self.y+2, self.x+BLOCK-2, self.y+BLOCK-2,
                                              fill='brown', width=2)

class Empty():
    def __init__(self, canvas, x, y):
        self.x = BLOCK * x
        self.y = BLOCK * y

class Snake():
    def __init__(self, name, canvas, field, x, y):
        self.name = name
        self.canvas = canvas
        self.field = field
        self.direction = random.randint(0,3)
        self.size = 3
        self.grow = 0
        self.body = []
        (u, v) = direction[self.direction]
        for k in range(self.size, 0, -1):
            self.add_cell(x - k * u, y - k * v)

    def add_cell(self, x, y):
        cell = self.canvas.create_oval(
            x*BLOCK, y*BLOCK, (x+1)*BLOCK, (y+1)*BLOCK,
            fill = 'yellow')
        self.body.insert(0, (x, y, cell))

    def move(self):
        (u, v) = direction[self.direction]
        x = self.body[0][0] + u
        y = self.body[0][1] + v
        if self.field.is_empty(x,y):
            if self.grow > 0:
                self.grow -= 1
                self.add_cell(x, y)
            else:
                # Reuse the last one
                self.canvas.itemconfigure(self.body[0][2], fill='green')
                cell = self.body.pop()[-1]
                self.canvas.coords(cell, x*BLOCK, y*BLOCK, (x+1)*BLOCK, (y+1)*BLOCK)
                self.canvas.itemconfigure(cell, fill='yellow')
                self.body.insert(0, (x, y, cell))

    def turn(self):
        if random.randint(0,10) < 2:
            if random.randint(0,1) == 1:
                self.direction = left(self.direction)
            else:
                self.direction = right(self.direction)
                
class Mouse():
    def __init__(self, canvas, x, y):
        self.widget = canvas.create_oval(
            x*BLOCK+2, y*BLOCK+2, (x+1)*BLOCK-2, (y+1)*BLOCK-2,
            fill = 'gray')

class Field():
    """Playing field for the snakes."""

    def __init__(self, canvas, width, height):
        self.width = width
        self.height = height
        self.canvas = canvas
        self.field = [[None] * height] * width
        for i in range(width):
            self.field[i][0] = Wall(canvas, i, 0)
            self.field[i][height-1] = Wall(canvas, i, height-1)
        for j in range(1, height-1):
            self.field[0][j] = Wall(canvas, 0, j)
            self.field[width-1][j] = Wall(canvas, width-1, j)
        for i in range(1, width-1):
            for j in range(1, height-1):
                self.field[i][j] = Empty(canvas, i, j)

    def is_empty(self, x, y):
        return (0 <= x < self.width and
                0 < y < self.height and
                isinstance(self.field[x][y], Empty))
                
    def find_empty(self):
        for i in range(5):
            x = random.randint(1, self.width-2)
            y = random.randint(1, self.height-2)
            if self.is_empty(x, y):
                return (x,y)
        return (None, None)

    def new_mouse(self):
        (a,b) = self.find_empty()
        if a and b:
            self.field[a][b] = Mouse(self.canvas, a, b)

class SnakeGame():
    def __init__(self, master, width=50, height=30):
        self.master = master
        self.width = width
        self.height = height
        self.canvas = Canvas(master, width=width*BLOCK, height=height*BLOCK)
        self.canvas.grid(row=0, column=1)
        self.field = Field(self.canvas, width, height)
        self.snakes = [Snake('Test', self.canvas, self.field, width//2, height//2)]
        self.t = 0
        self.tick()

    def tick(self):
        if self.t % 10 == 0:
            self.field.new_mouse()
        for s in self.snakes:
            if self.t % 20 == 0:
                s.grow = 1
            s.turn()
            s.move()
        self.t += 1        
        self.canvas.after(100, self.tick)
        
# Main program

if __name__ == "__main__":
    root = Tk()
    app = SnakeGame(root)
    root.mainloop()
