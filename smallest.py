import sys

def smallest(l):

    smallest_so_far = sys.maxsize
    for x in l:
        if x < smallest_so_far:
            smallest_so_far = x
    return(smallest_so_far)


l = [15, 100, 2343,34, 343, 434]
print(smallest(l))


"""TAKEAWAY: the = is like a pointer, this variable => this value. It is not like the mathematical one where you can flip flop things from one side to the other with no difference. in the above problem, smallest becomes x. If you change their positions, the output of that function becomes a huge number.
REMEMBER: this variable ===>>>>> this value. Which side of the equals sign matters."""
