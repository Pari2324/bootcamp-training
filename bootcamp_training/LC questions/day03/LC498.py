# diagonal traversal
class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:

        diag = {}

        m = len(mat)
        n = len(mat[0])

       
        for i in range(m):
            for j in range(n):

                key = i + j

                if key not in diag:
                    diag[key] = []

                diag[key].append(mat[i][j])

        ans = []

        for key in range(m + n - 1):

            if key % 2 == 0:
                ans.extend(diag[key][::-1])
            else:
                ans.extend(diag[key])

        return ans