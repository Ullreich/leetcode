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
"""
import numpy as np
import stuff

def maxSumSubmatrix(matrix: list[list[int]], k: int) -> int:
    min_conv = 10**(-5)

    # do zeilen statt spalente for indexing purposes
    zeilensummen = [[sum(z[:k+1]) for k in range(len(z))] for z in matrix]
    spaltensumme = [[sum(z[:k+1]) for k in range(len(z))] for z in transpose(zeilensummen)]

    print(f"z = {zeilensummen}")
    #print(f"s = {spaltensumme}")

    print(zeilensummen)
    while len(zeilensummen[0])>1:
        while len(spaltensumme[0])>1:
            spaltensumme = change_s(spaltensumme)
            #print(spaltensumme)
        zeilensummen = change_z(zeilensummen)
        spaltensumme = [[sum(z[:k + 1]) for k in range(len(z))] for z in transpose(zeilensummen)]
        print(zeilensummen)

    return zeilensummen

def change_z(zeilensummen):
    ret = list()
    for zeile in zeilensummen:
        ret.append([i - zeile[0] for i in zeile[1:]])
    return ret

def change_s(spaltensumme):
    #transpose so i can reuse change_z
    #trans = transpose(spaltensumme)
    return change_z(spaltensumme)

def transpose(matrix):
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]


matrix = [[1,0,1],[0,-2,3]]
k = 2
(maxSumSubmatrix(matrix, k))

print("real one")
stuff.maxSumSubmatrix(matrix, k)
"""