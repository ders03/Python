"""if a = [ 2, 2, 3 ] and b = [ 7, 5, 6, 7 ] it returns [ 14, 10, 18, 7 ]"""

def largest(a, b):
    if len(a)>len(b):
        return(a)
    else:
        return(b)

def equalize(a, b):
    diff = abs(len(a) - len(b))
    ls = []
    for x in range(0, len(largest(a, b))):
        if len(a)>len(b):
            b.append(int("1"))
        elif len(b)>len(a):
            a.append(int("1"))
    ls.append(a)
    ls.append(b)
    return(ls)

def element_mul(a, b):
    want = equalize(a, b)
    ls = []
    for x in range(0, len(largest(a, b))):
        ls.append(a[x]*b[x])
    return(ls)
        
