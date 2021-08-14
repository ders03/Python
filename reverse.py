


a = [1, 2, 3, 4]
b = ["a", "b"]

def funct():
    global a
    global b
    result = (a[::-1] + b[::-1])
    return(result)



print(funct())
