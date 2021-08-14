from gui import Gui
import time


def main():
    gui = Gui()  # take over screen
    width = gui.get_width()  # gives bounds of screens
    height = gui.get_height()

    try:
        continuePlaying = True

        x = 0
        while continuePlaying:
            c = gui.get_keypress()
            if c != "":
                continuePlaying = False

            gui.clear()
            gui.draw_text("(- . -)", 15, x, "RED", "GREEN")
            gui.refresh()
            time.sleep(0.4)

            gui.clear()
            gui.draw_text("-\_(o - o)_/-", 15, x, "RED", "GREEN")
            time.sleep(0.4)

    except Exception as e:
        gui.quit()
        print(e)
        return

    gui.quit()


if __name__ == "__main__":
    main()
