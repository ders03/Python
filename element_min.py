a = [ 1, 5, 8, 7 ]
b = [ 8, 9, 2, 2] #it returns [ 1, 1, 2, 3]


def element_wise_minimum(a, b):
    ls = []
    for x in a and b:
        ls.append(min(b))
        b.remove(min(b))
        ls.append(min(a))
        a.remove(min(a))
    return(ls)



print(element_wise_minimum(a, b))
