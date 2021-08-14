"""
This module represents the apple that appears at random places on the screen.
"""
import random
from typing import List

from gui import Gui
from position import Position
import time
gui = Gui()
def rand_x():                                                  #x and y have
    x = random.randrange(1, gui.get_width() - 2)            #different bounds,
    return x                                                   #can't put both through
                                                               #same f and have full
def rand_y():                                                  #map coverage
    y = random.randrange(1, gui.get_height() - 2)
    return y

def rand_pos():
    r_x = random.randrange(1, gui.get_width() - 2)
    r_y = random.randrange(1, gui.get_height() - 2)
    return Position(r_x, r_y)

def collides(p, positions):
    """Return true if p is any of the positions in the list."""
    for position in positions:
        if p.get_x() == position.get_x() and p.get_y == position.get_y():
            return True
    return False


class Apple:
    """The apple's location is randomly generated."""
    position = Position(rand_x(), rand_y())
    def __init__(self):
        self.pos = self.position

    def draw(self, gui):
        gui.draw_text("*", self.position.get_x(), self.position.get_y(), "RED", "GREEN")

    def is_eaten(self):
            self.position = rand_pos()
