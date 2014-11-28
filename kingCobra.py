import random
from snake import *

# Barva glave in repa
COLOR_HEAD = '#000000'
COLOR_TAIL = '#B80000'

class KingCobra(Snake):
    def __init__(self, field, x, y, dx, dy):
        # Poklicemo konstruktor nadrazreda
        Snake.__init__(self,
            field = field,
            color_head = COLOR_HEAD,
            color_tail = COLOR_TAIL,
            x = x, y = y, dx = dx, dy = dy)
        # V konstruktor lahko dodate se kaksne atribute

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


        x = self.coords[0][0]
        y = self.coords[0][1]

#        print (self.dx)
#        print (self.dy)

        if random.randint(0,10) < 2:
            if random.randint(0,1) == 1:
                self.turn_left()
                return
            else:
                self.turn_right()
                return

        if x < y:
            if self.dx == 0 and self.dy == 1:
                self.turn_right()
            if self.dx == 0 and self.dy == -1:
                self.turn_left()
            if self.dx == 1 and self.dy == 0:
                pass
            if self.dx == -1 and self.dy == 0:
                self.turn_right()
        else:
            if self.dx == 0 and self.dy == 1:
                self.turn_left()
            if self.dx == 0 and self.dy == -1:
                self.turn_right()
            if self.dx == 1 and self.dy == 0:
                self.turn_right()
            if self.dx == -1 and self.dy == 0:
                pass
                
