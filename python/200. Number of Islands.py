def numIslands(grid: list[list[str]]) -> int:
    counter = 0

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j]=="1":
                greedy(grid, i, j)
                counter+=1
    return counter
def greedy(arr, i, j):
    # delete island
    arr[i][j] = "0"

    #check neighboring fields
    # right
    if j+1<len(arr[0]):
        if arr[i][j+1]=="1":
            greedy(arr, i, j+1)
    # down
    if i+1<len(arr):
        if arr[i+1][j]=="1":
            greedy(arr, i+1, j)
    # left
    if j-1>=0:
        if arr[i][j-1]=="1":
            greedy(arr, i, j-1)
    # up
    if i-1>=0:
        if arr[i-1][j]=="1":
            greedy(arr, i-1, j)


grid = [["1","0","1","1","0","1","1"]]

print(numIslands(grid))
print(grid)