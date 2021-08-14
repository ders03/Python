def prod(l):
    init = l[0]
    for x in l:
        init = init * x
    return(init)


l = [1, 4, -6, 8]
print(prod(l))
