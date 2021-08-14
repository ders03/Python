

def sum_to_n(num):
    init = 0
    ls = []
    for i in range(0, (num)):
        init = i + init + 1
    return(init)


#print(sum_to_n(3))

import sys
def reverse_string(string):
    ls = []
    for x in range(int(len(string))-1, -1, -1):
        ls.append(string[x])
        end = ''.join(ls)
    return(end)


print(reverse_string("check"))

        
