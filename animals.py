#returns sound for animal type

inp=input("Enter a kind of animal :")

def sound_sorter(inp):
    if inp.endswith("dog"):
        print("Woof")
    elif inp.endswith("cat"):
        print("Meow")
    elif len(inp) < 1:
        print("Not a valid input")
    else:
        print("Grunt")

sound_sorter(inp)
