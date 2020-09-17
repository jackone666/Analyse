def maxWith(matrix):
    maxlength = 0
    for i in matrix:
        if maxlength < i.__len__():
            maxlength = i.__len__()
    return maxlength
