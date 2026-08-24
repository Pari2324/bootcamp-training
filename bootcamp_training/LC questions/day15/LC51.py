#N-Queen
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ans = []
        board = [["."] * n for _ in range(n)]

        def isSafe(row, col):

            # Same column
            for r in range(row):
                if board[r][col] == "Q":
                    return False

            # Upper-left diagonal
            r, c = row - 1, col - 1
            while r >= 0 and c >= 0:
                if board[r][c] == "Q":
                    return False
                r -= 1
                c -= 1

            # Upper-right diagonal
            r, c = row - 1, col + 1
            while r >= 0 and c < n:
                if board[r][c] == "Q":
                    return False
                r -= 1
                c += 1

            return True

        def backtrack(row):

            if row == n:
                ans.append(["".join(r) for r in board])
                return

            for col in range(n):

                if isSafe(row, col):

                    board[row][col] = "Q"

                    backtrack(row + 1)

                    board[row][col] = "."

        backtrack(0)

        return ans
        