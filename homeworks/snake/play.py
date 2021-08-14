"""
This is the main program for the snake game.
"""

import time

from gui import Gui
from room import Room
from snake import Snake
from apple import Apple, rand_pos, rand_x, rand_y, collides

def main():
    try:
        # Create the new Gui and start it. This clears the screen
        # and the Gui now controls the screen
        gui = Gui()

        # Create the room, the snake and the apple.
        # You will need to change the constructors later to pass more
        # information to the Snake and Apple constructors
        room = Room(gui.get_width(), gui.get_height(), "#", "WHITE", "BLUE")
        snake = Snake()
        apple = Apple()
        print(snake.ls)
        #snake.grow()
        #print(snake.ls)
        apple_state = ""
        snake_state = ""
        # The main loop of the game. Use "break" to break out of the loop
        player_score = 0
        continuePlaying = True
        while continuePlaying:
            # Get a key press from the user
            c = gui.get_keypress()
            if apple_state == "True":
                apple.is_eaten()
                apple_state = ""

            #if snake_state == "GROW":
                #snake.grow()
                #snake_state = ""
            # Do something with the key press
            h_x = 0
            h_y = 0
            # if c == 'q':
            #     do something if the user wants to quit
            if c == "q":
                continuePlaying = False
            elif c in ["w", "a", "s", "d"]:
                snake.change_direction(c)

            # elif c == "KEY_UP":
            #   do something depending on what was pressed,
            #     e.g. you may want to change the direction of the snake
            # elif c == "KEY_DOWN":
            #     do something else
            #if snake_state == "":
                #snake.move()
            if snake_state != "GROW":
                snake.move()
            else:
                pass
                #snake.grow()
                #snake_state = ""
            #snake.move()
            h_x += snake.current_pos().get_x()
            h_y += snake.current_pos().get_y()
            # Add your code to move the snake
            # around the screen here.
            # snake.move();

            # The redraw part of the game. First clear the screen
            gui.clear()
            if snake_state == "GROW":
                snake.grow()
                snake_state = ""

            # Redraw everything on the screen into an offscreen buffer,
            # including the room, the Snake and the apple
            room.draw(gui)
            apple.draw(gui)
            snake.draw(gui)

            # When done redrawing all the elements of the screen, refresh will
            # make the new graphic appear on the screen all at once
            gui.refresh()

            # Detect whether the snake ate the apple, or it hit the wall
            # or it hit its own tail here
            #snake_state = ""
            if h_x == apple.position.get_x() and h_y == apple.position.get_y():
                player_score += 10
                time.sleep(0.2)
                apple_state = "True"
                snake_state = "GROW"
                gui.clear()
                #snake.move()
                apple.draw(gui)
                room.draw(gui)
                #snake.draw(gui)

                gui.refresh()

            # This call makes the program go quiescent for some time, so
            # that it doesn't run so fast. If the value in the call to
            # time.sleep is decreased, the game will speed up.
            time.sleep(0.1)

    except Exception as e:
        
        # Some error occured, so we catch it, clear the screen,
        # print the log output, and then reraise the Exception
        # This will cause the program to quit and the error will be displayed

        gui.quit()
        raise e

    # Stop the GUI, clearing the screen and restoring the screen
    # back to its original state. Print the saved log output

    gui.quit()

    # The game has ended since we broke out of the main loop
    # Display the user's score here
    # Put an animation here for those things
    print(len(snake.inside))
    print()
    if player_score < 30:
        print("Your score was: " + str(player_score) + " (- . -)")
        print("Warm those fingers up, you'll do better next time!")
    elif 30 < player_score < 100:
        print("Your score was: " + str(player_score) + " <(^ - ^)^")
    elif player_score > 100:
        print("Your score was: " + str(player_score) + "（╯°□°）╯︵ ┻━┻")
if __name__ == "__main__":
    main()
