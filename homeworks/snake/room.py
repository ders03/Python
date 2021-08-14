"""
This module implements the four walls of the room within which Snake is played.
"""

from gui import Gui

class Room:
    """The room has a width and height, a character to draw, and color."""

    def __init__(self, width, height, c,
            fore_color, back_color):
        self.width = width
        self.height = height
        self.c = c
        self.fore_color = fore_color
        self.back_color = back_color

    def draw(self, gui):
        #Top
        gui.draw_line(self.c, 0, 0, self.width - 1, 0,
             self.fore_color, self.back_color)
        #Bottom
        gui.draw_line(self.c, 0, self.height - 1, self.width - 1, self.height-1,
            self.fore_color, self.back_color)
        #Left
        gui.draw_line(self.c, 0, 1, 0, self.height - 2,
            self.fore_color, self.back_color)
        #Right
        gui.draw_line(self.c, self.width - 1, 1, self.width - 1, self.height - 2,
            self.fore_color, self.back_color)    
