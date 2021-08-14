def length(s):
    if s == "":
        return 0
    return 1 + length(s[1:])

def main():
    print(length("Wherefore art thou Romeo"))

if __name__ == "__main__":
    main()


""" Pretty much, you just tell your self,
 this does this, call it like it will, and it works"""
