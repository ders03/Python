from gui import Gui

def main():
    gui = Gui()
    print("Screen width is: " + str(gui.get_width()))
    print("Screen height is: " + str(gui.get_height()))

if __name__ == "__main__":
    main()

