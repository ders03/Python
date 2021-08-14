from gui import Gui
import time
from random import random,seed,randint

gui = Gui()
class Unlimited_animated_objects(Gui):
    def __init__(self, num, x=gui.get_width()//2, y=gui.get_height()//2, ):
        self.x = int(x)
        self.y = int(y)
        self.num = int(num)
        #ls = []
        #ls.append("*"*self.num)

    def update(self):
        result = randint(-2, 2)
        self.x += result
        self.y += result

    def animate_list(self):
        ls = []
        ls.append("*"*self.num)
        for obj in ls:
            try:
                while True:
                    gui.clear()
                    self.update()

                    gui.draw_text(obj, self.x, self.y, "RED", "BLACK" )

                    gui.refresh()
                    time.sleep(0.5)
                    gui.clear()
                    self.update()

                    gui.draw_text(obj, -self.x, self.y, "BROWN", "ORANGE")

                    gui.refresh()
                    time.sleep(0.5)
                    gui.clear()

                    end = gui.get_keypress()
                    if end != "":
                        break

            except Exception as e:
                gui.quit()
                raise e
            gui.quit()

def main():

    Unlimited_animated_objects(4).animate_list()
    print(Unlimited_animated_objects(4).update())

if __name__ == "__main__":
    main()







