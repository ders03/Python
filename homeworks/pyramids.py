def pyramid(number):
    result = []
    #strip into list
    for x in range(1, int(number+1)):
            result.append("*"*x)
    #join by "\n"
    return("\n".join(result))

def side_pyramid(row): 
        j = row
        going_up = []
        going_down = []
        #for loop gets us to mid of pyramid
        for x in range(1, row+1):
            # iterates back down
            j = j - 1
            going_up.append("*"*x)
            going_down.append("*"*j)
        #snip off char at [0], adds extra space to printout
        return("\n".join(going_up+going_down[:-1]))

#similar strat to side_pyramid, need to add spaces on iterator instead of walking back down
def alternating_pyramid(rows):
    j = rows
    ls = []
    for y in range(1, rows+1):
        #starts at bottom row, with zero spaces, next row has one space, etc.
        j = j - 1
        #goes line by line and puts (row above - 1) spaces into row then adds the bits I want
        star_string =(" "*j + "*+"*y)
        #goes line by line and cuts off un wanted star
        ls.append(star_string[:-1])
    return("\n".join(ls))

#checks everything at funct(0)
def main():
    x = 0
    pyramid(x)
    side_pyramid(x)
    alternating_pyramid(x)


if __name__ == "__main__":
    main()
