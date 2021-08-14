

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_width(self):
        return self.width

    def get_height(self):
        return(self.height)

    def area(self):
        return(int(self.width) * int(self.height))

class Square(Rectangle):
    def __init__(self, width):
        super().__init__("Square")




def main():
    test = Square(5, 5)
    print(Square(5, 5))
    print(test.area(self))

    if __name__ == "__main__":
        main()
