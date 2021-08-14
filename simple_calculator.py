import sys






def calculate():
    try:
        if len(sys.argv[1]) and len(sys.argv[2]) > 0:
            x = int(sys.argv[1]) + int(sys.argv[2])
            print(x)
    except IndexError:
        print("usage: python3 solution.py OP1 OP2")

calculate()
