def substring(word, index1, index2):
    ls = []
    for letter in range(index1, index2):
        ls.append(word[letter])
    return("".join(ls))

print(substring("hamburger", 4, 8))
        
