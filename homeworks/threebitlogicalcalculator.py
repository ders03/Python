def one_bit_NOT(c):
    if not c == "1":
        return"1"
    else:
        return"0"

def one_bit_OR(a,b):
    if a == "1" or b == "1":
        return"1"
    else:
        return"0"

def one_bit_AND(a,b):
    if a =="1" and b =="1":
        return"1"
    else:
        return"0"

def three_bit_AND(a,b):
    #split string to run through one bit functions
    a = list(a)
    b = list(b)
    #rejoin function output to string
    return(one_bit_AND(a[0], b[0])+one_bit_AND(a[1], b[1])+one_bit_AND(a[2], b[2]))

def three_bit_OR(a,b):
    #same strat
    a = list(a)
    b = list(b)
    return(one_bit_OR(a[0], b[0])+one_bit_OR(a[1], b[1])+one_bit_OR(a[2], b[2]))

def three_bit_NOT(s):
    #same strat
    c = list(s)
    return(one_bit_NOT(c[0])+one_bit_NOT(c[1])+one_bit_NOT(c[2]))



def main():
    #define inputs and define cases to run inputs through functions
    input_operation = input("Enter operation (NOT, AND, OR): ")

    if input_operation == ("AND"):
        input_number1 = input("Enter number 1 :")
        input_number2 = input("Enter number 2 :")
        print("Answer " + three_bit_AND(input_number1, input_number2))


    elif input_operation == ("OR"):
        input_number1 = input("Enter number 1 :")
        input_number2 = input("Enter number 2 :")
        print("Answer " + three_bit_OR(input_number1, input_number2))


    elif input_operation == ("NOT"):
        input_number = input("Enter number :")
        print("Answer " + three_bit_NOT(input_number))

if __name__ == "__main__":
    main()
