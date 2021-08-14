#return first and last chars in string

string = input("Enter a word or sentence :")

def sorter():
    try:
        print("Ends with " + string[len(string)-1])
        print("Begins with " + string[0])
    except IndexError:
        print("None", "None")
sorter()
