#!/usr/bin/python

import random

BLOCK = 20

# Helper functions

def brick(canvas, x, y):
    """Create a brick widget (to be placed on the edge of the field)."""
    return canvas.create_rectangle(x*BLOCK, y*BLOCK, (x+1)*BLOCK, (y+1)*BLOCK,
                                   fill='brown', width=2)
def mouse(canvas, x, y):
    """Create a mouse widget."""
    return canvas.create_oval(x*BLOCK+2, y*BLOCK+2, (x+1)*BLOCK-2, (y+1)*BLOCK-2,
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
            self.add_cell(x - k * self.dx, y - k * self.dy)
        self.add_cell(x, y) # the head

    def add_cell(self, x, y):
        cell = self.field.canvas.create_oval(
            x*BLOCK, y*BLOCK, (x+1)*BLOCK, (y+1)*BLOCK, fill = self.color_head)
        if len(self.cells) > 0:
                self.field.canvas.itemconfigure(self.cells[0], fill=self.color_tail)
        self.coords.insert(0, (x, y))
        self.cells.insert(0, cell)
                        
    def turn_left(self):
        """Rotate a vector by pi/2 anticlockwise."""
        (self.dx, self.dy) = (-self.dy, self.dx)

    def turn_right(self):
        """Rotate a vector by pi/2 clockwise."""
        (self.dx, self.dy) = (self.dy, -self.dx)
            
    def move(self):
        (x,y) = self.coords[0]
        x += self.dx
        y += self.dy
        if self.field.is_mouse(x,y):
            self.grow = 1
            self.field.remove_mouse(x,y)
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
        pass

                
class Field():
    """Playing field for the snakes."""

    def __init__(self, canvas, width, height):
        self.width = width
        self.height = height
        self.canvas = canvas
        self.snakes = []
        self.mice = {}
        self.bricks = []
        # The bricks
        for i in range(width):
            self.bricks.append(brick(canvas, i, 0))
            self.bricks.append(brick(canvas, i, height-1))
        for j in range(1, height-1):
            self.bricks.append(brick(canvas, 0, j))
            self.bricks.append(brick(canvas, width-1, j))

    def add_snake(self, s):
        s.id = len(self.snakes)
        self.snakes.append(s)
    
    def is_mouse(self, i, j):
        return (0 < i < self.width-1 and
                0 < j < self.height-1 and
                (i,j) in self.mice)
    
    def is_empty(self, i, j):
        if (0 < i < self.width-1 and
            0 < j < self.height-1 and
            (i,j) not in self.mice):
            for s in self.snakes:
                if (i,j) in s.coords: return False
            return True
        else:
            return False
                            
    def find_empty(self):
        for i in range(5):
            x = random.randint(1, self.width-2)
            y = random.randint(1, self.height-2)
            if self.is_empty(x, y):
                return (x,y)
        return (None, None)

    def new_mouse(self):
        (x,y) = self.find_empty()
        if x and y:
            self.mice[(x,y)] = mouse(self.canvas, x, y)

    def remove_mouse(self, x, y):
        m = self.mice.get((x,y))
        if m:
            self.canvas.delete(m)
            del self.mice[(x,y)]
