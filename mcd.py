

def can_buy(n):
    #base case
    if n < 4:
        return False
    if n == 4 or n == 15:
        return True

    #recursive leap
    return can_buy(n - 4) or can_buy(n - 15)

    #This finds all possible paths down to 0 using 4 or 15
