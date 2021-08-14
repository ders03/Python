

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def get_length(self):
        return(rect.length)

    def get_width(self):
        return(self.width)

    def area(self):
        return self.length * self.width







def main():
    rect = Rectangle(5, 9)
    print(rect.area())

if __name__ == "__main__":
    main()
