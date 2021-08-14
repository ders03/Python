

def erase_character(word, char):
    ls = []
    for letter in word:
        if letter == char:
            ls.append("_")
        else:
            ls.append(letter)
    return("".join(ls))

print(erase_character("banana", "n"))
