

vowels = ("a, e, i, o, u, y, A, E, I, O, U")

def remove(string):
    init = ""
    for letter in string:
        if letter.lower() in vowels:
            init = init + ""
        else:
            init = init + letter
    return(init)

print(remove("Taco Bell"))
