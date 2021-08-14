#julien@localhost$ python3 solution.py antoine
#antoine
#julien@localhost$ python3 solution.py julien
#julien
#julien@localhost$ python3 solution.py
#usage: python3 solution.py PARAM
#julien@localhost$
#If there is no parameters given, it should print the following error message:

#usage: python3 solution.py PARAM

import sys

#custom error build



for arg in sys.argv[0:1]:
    try:
        print(sys.argv[1])

    except IndexError:
            print("PARAM")
