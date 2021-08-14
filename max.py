#find largest in a string

def max_in(numbers):
    #initial largest value is 0
    largest_so_far = 0
    for x in numbers:
        if x>largest_so_far:
            largest_so_far = x
    return(largest_so_far)



numbers = [1, 2, 42, 17]
print(max_in(numbers))
