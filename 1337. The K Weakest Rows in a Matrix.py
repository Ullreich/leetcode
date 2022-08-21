def kWeakestRows(mat: list[list[int]], k: int) -> list[int]:
    # associate index with strength
    l = [[i, sum(mat[i])] for i in range(len(mat))]
    # sort by strength, which is in the second column
    l.sort(key=lambda x: x[1])
    #return the first k indexes
    ind = [x[0] for x in l[:k]]
    return ind

a = [[1,1,0,0,0],
     [1,1,1,1,0],
     [1,0,0,0,0],
     [1,1,0,0,0],
     [1,1,1,1,1]]

b = [[1,0,0,0],
     [1,1,1,1],
     [1,0,0,0],
     [1,0,0,0]]

print(kWeakestRows(b, 2))