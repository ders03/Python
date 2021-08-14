num = input()

#only way that actually puts it in a list so far, would like to use sys.stdin
def raw():
    lines = []
    for sentence in range(int(num)):
        lines.append(input())
    return(lines)

#hardset
para = raw()

#find longest for formatting
def longest(x):
    init = 0
    for line in para:
        if len(line)>init:
            init = len(line)
    return(init)

def lengthen():
    longer = []
    for line in para:
        longer.append(line + " "*(longest(para)-len(line)))
    return(longer)

same_length = lengthen()

def format_():
    header = "++++" + "+"*longest(para)
    formatted = [header]
    for line in same_length:
        formatted.append("+ " + line + " +")
    formatted.append(header)
    return(formatted)

for line in format_():
    print(line)


    
