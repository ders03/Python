"""Write a function subtract(s, t) that returns a string where all characters in t are removed from s, independent of case.

For example, if s is "Magnificent Fying Penguins", and t is "maG", then the function would return "nificent Flyin Penuins"."""
import string

def subtract(s, t):
    init = ""
    j = 0
    for letter in s:
        j = j + 1
        if letter.lower() not in t.lower():
            init = init + letter
    return(init)


s = "MAGNIFICENT Flying Penguins"
t = ""
print(subtract(s, t))
