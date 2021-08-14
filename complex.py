

class Complex:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __str__(self):
        if self.imaginary >= 0:
            return str(self.real) + "+" + str(self.imaginary) + "i"
        else:
            return str(self.real) + str(self.imaginary) + "i"

    def getReal(self):
        return self.real

    def getImaginary(self):
        return self.imaginary

    def negate(self):
        self.real = -1*int(self.real)
        self.imaginary = -1*int(self.imaginary)
        return Complex.__str__(self)

    def add(self, c2):
        real = int(self.real) + int(c2.real)
        imaginary = int(self.imaginary) + int(c2.imaginary)
        if imaginary >= 0:
            return str(real) + "+" + str(imaginary) + "i"
        else:
            return str(real) + str(imaginary) + "i"

    def mul(self, c2):
        real = int(self.real)*int(c2.real) - int(self.imaginary)*int(c2.imaginary)
        imaginary = int(self.real)*int(c2.imaginary) + int(self.imaginary)*int(c2.real)
        if imaginary >= 0:
            return str(real) + "+" + str(imaginary) + "i"
        else:
            return str(real) + str(imaginary) + "i"



def main():
    c1 = Complex(3, 4)
    c2 = Complex(2, -9)
    print(c1.add(c2))
    print(c1.mul(c2))
    #print(c.negate())
if __name__ == "__main__":
    main()
