import random
from snake import *

COLOR_HEAD = 'red'
COLOR_TAIL = 'orange'

class BolivianAnaconda(Snake):
    def __init__(self, field, x, y, dx, dy):
        Snake.__init__(self,
            field = field,
            color_head = COLOR_HEAD,
            color_tail = COLOR_TAIL,
            x = x, y = y, dx = dx, dy = dy)

    def turn(self):
        if random.randint(0,10) < 5:
            if random.randint(0,1) == 1:
                self.turn_left()
            else:
                self.turn_right()

