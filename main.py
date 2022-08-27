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