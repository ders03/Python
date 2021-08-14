def listmax(a):
    """Max value iterative solution"""
    largestSoFar = 0
    for ele in a:
        if largestSoFar < ele:
            largestSoFar = ele
    return largestSoFar


def listmax_recur(a):
    if a == []:
        return 0

    largestInRestOfList = listmax_recur(a[1:])
    if a[0] < largestInRestOfList:
        return largestInRestOfList
    else:
        return a[0]
