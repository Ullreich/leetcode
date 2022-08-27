import numpy as np
from scipy import signal

#this solves it but not very fast

def maxSumSubmatrix(matrix: list[list[int]], k: int) -> int:
    m = len(matrix)
    n = len(matrix[0])
    b = np.array(matrix)
    max_smaller = -np.infty

    indexes = list()

    # find all possible indexes
    for i in range(1, m+1):
        for j in range(1, n+1):
            indexes.append([i, j])

    # convolve over matrix
    for ones in indexes:
        conv = signal.convolve2d(b, np.ones(ones), "valid")
        # return k if k in the convolution
        print(conv)
        if k in conv:
            return k
        # find the maximal element of the convolution that is smaller than k
        else:
            # check if any of the elements in the convolution are smaller than k
            if np.any([conv<k]):
                max_conv = np.max(conv[conv<k])
                max_smaller = max(max_conv, max_smaller)
    #print(max_smaller)
    return int(max_smaller)

#print(maxSumSubmatrix(a, b))

#b = np.array(a)
#print(b)

#idea: get all possible indexes and then convolve that over the matrix
#get_indexes


#ones = np.ones([2,2])
#print(ones)

#print(signal.convolve2d(b, ones, "valid"))

"""
def maxSumSubmatrix(matrix: list[list[int]], k: int) -> int:
    min_conv = -np.infty

    while len(matrix):
        min_conv = sub(matrix, min_conv, k)
        matrix.pop(0)

    return min_conv

def sub(matrix, min_conv, k):
    l = len(matrix[0])
    h = len(matrix)

    for ind in range(l):
        for r in range(ind,l):
            bar = 0
            for d in range(h):
                foo = matrix[d]
                #print(foo[ind:r+1])
                baz = sum(foo[ind:r + 1])
                if baz > min_conv and baz <= k:
                    min_conv = baz
                bar += baz
                #print(bar)
            if bar > min_conv and bar <= k:
                min_conv = bar
    return min_conv

matrix = [[27,5,-20,-9,1,26,1,12,7,-4,8,7,-1,5,8],[16,28,8,3,16,28,-10,-7,-5,-13,7,9,20,-9,26],[24,-14,20,23,25,-16,-15,8,8,-6,-14,-6,12,-19,-13],[28,13,-17,20,-3,-18,12,5,1,25,25,-14,22,17,12],[7,29,-12,5,-5,26,-5,10,-5,24,-9,-19,20,0,18],[-7,-11,-8,12,19,18,-15,17,7,-1,-11,-10,-1,25,17],[-3,-20,-20,-7,14,-12,22,1,-9,11,14,-16,-5,-12,14],[-20,-4,-17,3,3,-18,22,-13,-1,16,-11,29,17,-2,22],[23,-15,24,26,28,-13,10,18,-6,29,27,-19,-19,-8,0],[5,9,23,11,-4,-20,18,29,-6,-4,-11,21,-6,24,12],[13,16,0,-20,22,21,26,-3,15,14,26,17,19,20,-5],[15,1,22,-6,1,-9,0,21,12,27,5,8,8,18,-1],[15,29,13,6,-11,7,-6,27,22,18,22,-3,-9,20,14],[26,-6,12,-10,0,26,10,1,11,-10,-16,-18,29,8,-8],[-19,14,15,18,-10,24,-9,-7,-19,-14,23,23,17,-5,6]]
k = -101
#corrext one
print(stuff.maxSumSubmatrix(matrix, k))

print(matrix)
print(maxSumSubmatrix(matrix, k))
"""