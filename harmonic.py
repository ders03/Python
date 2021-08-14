


def harmonic(n):
    init = 0
    for x in range(1, n+1):
        init = init + x**-1
    return(init)


print(harmonic(5))
