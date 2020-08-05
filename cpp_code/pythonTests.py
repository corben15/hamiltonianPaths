import math
def generate_start_list(n=3):
    half_n = math.ceil(n/2)
    startList = []
    startIndex = 0
    endIndex = half_n
    rowlength = half_n
    for i in range(half_n):
        print(list(range(rowlength)))
        for j in range(rowlength):
            startList.append(startIndex + j)
        endIndex = endIndex + n
        rowlength -= 1
        startIndex = endIndex - rowlength
    return startList


generate_start_list(4)
