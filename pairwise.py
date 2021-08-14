a = [ "dog", "cat", "goat" ]
b = ["carrot", "lettuce", "tomato"]

def pair_wise(a, b):
    ls = []
    for x in a:
        for y in b:
            ls.append(x + ", " + y)
    return("\n".join(ls))



print(pair_wise(a, b))
