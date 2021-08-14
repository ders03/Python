"""
This module implements the snake class.
"""

from gui import Gui
from position import Position
from typing import List

class Snake:
    """This is the Snake.

    It has a list of positions. The head is at index 0.
    The tail occupies the rest of the list.
    """
    gui = Gui()
    init_head = Position(gui.get_width()//2, gui.get_height()//2)
    init_tail = Position(init_head.get_x() -1, init_head.get_y())
    init_tail2 = Position(init_head.get_x() - 2, init_head.get_y())
    snake_p = [init_head, init_tail, init_tail2]
    ls_c = [">", "+", "+"]
    #snake contains positions as snake moves in the following format:
    #[Position(first_step_right.xpos,first_step_right.ypos), current length of snake]
    #SO snake[0, 2, 4, 6...] = Position object (len(snake) - 2 = current_pos)
    #   snake[1, 3, 5, 7...] = length of snake (len(snake) - 1 = current length of snake)
    snake = [init_tail2, 3, init_tail, 3, init_head, 3]
    def __init__(self, direction="d"):
        self.ls = self.ls_c
        self.direction = direction
        self.inside = self.snake_p


    def current_pos(self):
        return self.snake[len(self.snake) - 2]

    def current_len(self):
        return self.snake[len(self.snake) - 1]

    #range(len(self.snake):x:-2)


    #THIS POINTS TO THE POSITION AT THE TAIL WHEN I GROW IT
    #snake[len(self.snake) - (current_len() + 1)*2)], 1 will give head pos, 2 tail pos, etc.!!!!!!


    #snake[len(self.snake) - 2]
    #snake[len(self.snake) - 4]
    #snake[len(self.snake) - 6]
    #snake[(len(self.snake) - 1) - len(self.ls_c - 1)*2]



    def draw(self, gui):
        if self.direction == "d":
            self.ls[0] = ">"
            for x in range(self.current_len() - 1, -1, -1):
                gui.draw_text(
                self.ls_c[x], self.snake[len(self.snake) - (x+1)*2].get_x(), self.snake[len(self.snake) - (x+1)*2].get_y(), "YELLOW", "RED"
                )
        if self.direction == "a":
            self.ls[0] = "<"
        if self.direction == "w":
            self.ls[0] = "^"
        if self.direction == "s":
            self.ls[0] = "V"
        #for x in range(len(self.ls) - 1, -1, -1):
            #gui.draw_text(self.ls[x], self.inside[x].get_x(), self.inside[x].get_y(), "RED", "YELLOW")

        j = -1
        for position in self.inside:
            j+=1
            print(position.get_x(), position.get_y())
            #j += 1
            #gui.draw_text(self.ls[j], position.get_x(), position.get_y(), "RED", "YELLOW")



    def move(self):
        """Check for direction, define the positions relevant to the length of
           the snake at the current time, redefine init positions to rely on head,
           init head movement """
        #Move up on keypress
        if self.direction == "w":
            for x in range(len(self.ls)-1, 0, -1):               # KEEP FOR LOOP
                self.inside[x].xpos = self.inside[x-1].xpos    # HERE instead of
                self.inside[x].ypos = self.inside[x-1].ypos    # play keeps debugging simple
            self.inside[0].ypos -= 1
            #self.snake.append(self.inside[0])
            self.snake.append(len(self.ls))
        #Move down on keypress                                   #xpos mods position,
        if self.direction == "s":                                #getters in position file
            for x in range(len(self.ls)-1, 0, -1):               #just return current value
                self.inside[x].xpos = self.inside[x-1].xpos
                self.inside[x].ypos = self.inside[x-1].ypos
            self.inside[0].ypos += 1
            self.snake.append(self.init_head)
            self.snake.append(len(self.ls))
        #Move left on keypress
        if self.direction == "a":
            for x in range(len(self.ls)-1, 0, -1):
                self.inside[x].xpos = self.inside[x-1].xpos
                self.inside[x].ypos = self.inside[x-1].ypos
            self.inside[0].xpos -= 1
            self.snake.append(self.init_head)
            self.snake.append(len(self.ls))
        #Move right on keypress
        if self.direction == "d":
            for x in range(len(self.ls)-1, 0, -1):
                self.inside[x].xpos = self.inside[x-1].xpos
                self.inside[x].ypos = self.inside[x-1].ypos
            self.inside[0].xpos+=1
        self.snake.append(self.init_head)
        self.snake.append(len(self.ls))

    def change_direction(self, direction_string):
        if self.direction in ["a", "d"] and direction_string not in ["a", "d"]:
            self.direction = direction_string
        elif self.direction in ["w", "s"] and direction_string not in ["w", "s"]:
            self.direction = direction_string

    def grow(self):
        self.ls_c.append("+")
        new_pos = Position(self.inside[len(self.inside) - 2].get_x(), self.inside[len(self.inside) - 2].get_y())
        self.snake_p.append(new_tail_pos)


snake = Snake()
for position in snake.snake[0::2]:
    print(position.get_x(), position.get_y())

snake.move()
for position in snake.snake[0::2]:
    print(position.get_x(), position.get_y())
