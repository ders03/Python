import string
s = "Magnificent Flying Penguins"
def subtract(s, t):
    ls = []
    for letter in s:

        if letter.lower() not in t.lower():
            ls.append(letter)
        else:
            pass
    return("".join(ls))

print(subtract(s, "maG"))

def main():
    subtract(s, t)
    if __name__ == "__main__":
        main()
