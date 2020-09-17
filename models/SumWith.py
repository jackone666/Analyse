def sumWith(level):
    totalWith = 0
    for i in level:
        totalWith += i.__len__()
    return totalWith
