import random
from snake import *

# Barva glave in repa
COLOR_HEAD = '#502B19'
COLOR_TAIL = '#A37519'

class DwarfBoa(Snake):
    def __init__(self, field, x, y, dx, dy):
        # Poklicemo konstruktor nadrazreda
        Snake.__init__(self,
            field = field,
            color_head = COLOR_HEAD,
            color_tail = COLOR_TAIL,
            x = x, y = y, dx = dx, dy = dy)
        # V konstruktor lahko dodate se kaksne atribute
        dx = 0
        dy = x%2
        dy = 1 if dy == 1 else -1
        print(x, dy)

    def turn(self):
        """Igrica poklice metodo turn vsakic, preden premakne kaco. Kaca naj se tu odloci, ali se
           bo obrnila v levo, v desno, ali pa bo nadaljevala pot v isti smeri.

           * v levo se obrne s self.turn_left()
           * v desno se obrne s self.turn_right()
           * koordinate glave so self.coords[0]
           * smer, v katero potuje je (self.dx, self.dy)
           * spisek koordinat vseh misk je self.field.mice.keys()
           * spisek vseh kac je self.field.snakes
        """
        xH = self.coords[0][0]
        yH = self.coords[0][1]
        dx = self.dx
        dy = self.dy
        print(xH,yH,dx,dy)
        if dx == 0:
            if xH%2 == 1:
                self.dy = 1
            else:
                self.dy = -1

            if yH == 28:
                self.turn_right()
                print(self.dx)
            if yH == 2:
                self.turn_left()
                print(self.dx)
        else:
            if yH == 28:
                self.turn_right()
            elif yH == 2:
                self.turn_left()
    
