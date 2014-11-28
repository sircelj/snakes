import random
from snake import *

COLOR_HEAD = '#0000ff'
COLOR_TAIL = '#000080'

class CongoWaterCobra(Snake):
    def __init__(self, field, x, y, dx, dy):
        Snake.__init__(self,
            field = field,
            color_head = COLOR_HEAD,
            color_tail = COLOR_TAIL,
            x = x, y = y, dx = dx, dy = dy)
        self.i = 0
        
    def turn(self):
        self.i -= 1
        if self.i <= 0:
            self.turn_left()
            self.i = 10
