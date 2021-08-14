def peel(n):
    if n == []:
        print("No onion left, start cooking")
        return

        print("Peeling " + str(n[0]))
        rest = n[1]
        peel(rest)

def main():
    onion = [6, 5, 4, 3, 2, 1, 0]
    peel(onion)

if __name__ == "__main__":
    main()
