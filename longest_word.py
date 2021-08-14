import datetime

def longboi(x, y, z):
    if len(x) > len(y) and len(z):
        print(x)
    if len(z) > len(x) and len(y):
        print(z)
    elif len(y) > len(x) and len(z):
        print(y)




#longboi("test", "tom cruise", "hemmingsworth")

def is_triangle(s1, s2, s3):
    sides = [s1, s2, s3]
    if sides[0] + sides[1] > sides[2] or sides[1] + sides[2] > sides[0] or sides[2] + sides[0] > sides[1]: return(True)
    else:
        return(False)

#print(is_triangle(0, 1, 4))


def american():
    today = datetime.datetime.now()
    print(today.strftime("%A, %B %d, %Y"))

american()

def european():
    today = datetime.datetime.now()
    print(today.strftime("%A, %d %B, %Y"))

def is_special_number(x):
    if x%7 == 0 and not x%5 == 0:
        return(True)
    else:
        return(False)

def is_positive_special_number(x):
    if is_special_number(x)>=0:
        return(True)

    else:
        return(False)

print(is_positive_special_number(14))
