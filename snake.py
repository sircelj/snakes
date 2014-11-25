#!/usr/bin/python

from Tkinter import *
import random

BLOCK = 20

EMPTY = 0
BRICK  = 1
MOUSE = 2

def left(dx, dy):
    return (-dy, dx)

def right(dx, dy):
    return (dy, -dx)

def brick(canvas, x, y):
    return canvas.create_rectangle(x*BLOCK, y*BLOCK, (x+1)*BLOCK, (y+1)*BLOCK,
                                   fill='brown', width=2)
def mouse(canvas, x, y):
    canvas.create_oval(x*BLOCK+2, y*BLOCK+2, (x+1)*BLOCK-2, (y+1)*BLOCK-2,
                       fill = 'gray')

class Snake():
    def __init__(self, field, color_head, color_tail, x, y, dx, dy):
        self.field = field
        self.dx = dx
        self.dy = dy
        self.size = 3
        self.grow = 0
        self.color_head = color_head
        self.color_tail = color_tail
        self.coords = []
        self.cells = []
        # the tail
        for k in range(self.size-1, 0, -1):
            self.add_cell(x - k * self.dx, y - k * self.dy, head=False)
        self.add_cell(x, y) # the head

    def add_cell(self, x, y, head=True):
        cell = self.field.canvas.create_oval(
            x*BLOCK, y*BLOCK, (x+1)*BLOCK, (y+1)*BLOCK,
            fill = (self.color_head if head else self.color_tail))
        self.coords.insert(0, (x, y))
        self.cells.insert(0, cell)
                        
    def move(self):
        (x,y) = self.coords[0]
        x += self.dx
        y += self.dy
        if self.field.is_empty(x,y):
            if self.grow > 0:
                self.grow -= 1
                self.add_cell(x, y)
            else:
                # Reuse the last one
                self.coords.pop()
                self.coords.insert(0, (x,y))
                self.field.canvas.itemconfigure(self.cells[0], fill=self.color_tail)
                cell = self.cells.pop()
                self.field.canvas.coords(cell, x*BLOCK, y*BLOCK, (x+1)*BLOCK, (y+1)*BLOCK)
                self.field.canvas.itemconfigure(cell, fill=self.color_head)
                self.cells.insert(0, cell)

    def turn(self):
        if random.randint(0,10) < 2:
            if random.randint(0,1) == 1:
                (self.dx, self.dy) = left(self.dx, self.dy)
            else:
                (self.dx, self.dy) = right(self.dx, self.dy)
                
class Field():
    """Playing field for the snakes."""

    def __init__(self, canvas, width, height):
        self.width = width
        self.height = height
        self.canvas = canvas
        self.snakes = {}
        self.mice = {}
        self.bricks = []
        self.refresh_matrix()
        # The bricks
        for i in range(width):
            self.bricks.append(brick(canvas, i, 0))
            self.bricks.append(brick(canvas, i, height-1))
        for j in range(1, height-1):
            self.bricks.append(brick(canvas, 0, j))
            self.bricks.append(brick(canvas, width-1, j))

    def refresh_matrix(self):
        self.matrix = [[EMPTY for j in range(self.height)] for i in range(self.width)]
        for i in range(self.width):
            self.matrix[i][0] = BRICK
            self.matrix[i][self.height-1] = BRICK
        for j in range(1, self.height-1):
            self.matrix[0][j] = BRICK
            self.matrix[self.width-1][j] = BRICK
        for s in self.snakes.values():
            for (i,j) in s.coords():
                self.matrix[i][j] = s.id
        for (i,j) in self.mice:
            self.matrix[i][j] = MOUSE

    def is_empty(self, i, j):
        return (0 < i < self.width-1 and
                0 < j < self.height-1 and
                self.matrix[i][j] == EMPTY)
                
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
            self.mice[(a,b)] = mouse(self.canvas, a, b)

    def eat_mouse(self, (a, b)):
        m = self.mice.get((a,b))
        if m:
            self.canvas.delete(m)
            del self.mice[(a,b)]

class SnakeGame():
    def __init__(self, master, width=50, height=30):
        self.master = master
        self.width = width
        self.height = height
        self.canvas = Canvas(master, width=width*BLOCK, height=height*BLOCK)
        self.canvas.grid(row=0, column=1)
        self.field = Field(self.canvas, width, height)
        self.snakes = [Snake(self.field, 'yellow', 'red', width//2, height//2, -1, 0)]
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
        self.field.refresh_matrix()
        self.t += 1
        self.canvas.after(100, self.tick)
        
# Main program

if __name__ == "__main__":
    root = Tk()
    app = SnakeGame(root)
    root.mainloop()
