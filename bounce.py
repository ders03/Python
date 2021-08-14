from gui import Gui
import time
from random import random,seed

def main():
    gui = Gui()

    # initialize whatever you need to here
    width = gui.get_width()
    height = gui.get_height()
    seed(10)
    x = (width // 2) - 5
    x2 = (width // 2) + 5
    y = (height // 2) - 5
    y2 = (height // 2) + 5
    try:
        while True:
            # The screen is cleared at every iteration
            gui.clear()


            # draw the asterisk here
            gui.draw_text("*", x, y, "RED", "PURPLE")
            gui.draw_text("*", int(random()*10), y2-2, "GREEN", "BROWN")


            # The drawing is shown all at once
            gui.refresh()
            time.sleep(0.2)
            gui.clear()
            # update and move the asterisk here
            gui.draw_text("*", width-1, height-1, "GREEN", "BROWN")
            gui.draw_text("*", int(random())*10, y+4, "RED", "PURPLE")
            gui.refresh()
            time.sleep(0.2)
            gui.clear()
            # check keypress, and quit if user hits a key
            c = gui.get_keypress()
            if c != "":
                break

            # slow down the computer by sleeping for 1/10th of a sec
            #time.sleep(0.4)

    except Exception as e:
        # handle errors and clean up so the screen is restored
        gui.quit()
        raise e
    gui.quit()


if __name__ == "__main__":
    main()
