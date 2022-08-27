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
        #print(conv)
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