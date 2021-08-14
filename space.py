def white_space(s):
    init = 0
    for c in (s):
        if c == " ":
            init = init + 1
    return(init)

s = " saodon aosjdksdj okajskojd ok jksj okjokj"
print(white_space(s))
