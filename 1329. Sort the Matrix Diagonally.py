class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        # iterate through top
        mat
        l = len(mat[0])
        h = len(mat)

        # run through the top and sort that
        for i in range(l):
            swp = list()

            # run through once to get numbers
            for j in range(h):
                try:
                    swp.append(mat[j][i + j])
                except IndexError:
                    pass

            # replace with sorted
            swp.sort()
            for j in range(h):
                try:
                    mat[j][i + j] = swp[j]
                except IndexError:
                    pass

        # run though side and sort that
        for i in range(1, h):
            swp = list()

            # run through once to get numbers
            for j in range(h):
                try:
                    swp.append(mat[i + j][j])
                except IndexError:
                    pass

            # replace with sorted
            swp.sort()
            for j in range(h):
                try:
                    mat[i + j][j] = swp[j]
                except IndexError:
                    pass

        return mat
