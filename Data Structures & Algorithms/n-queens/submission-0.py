class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = ["." * n] * n
        res = []
        def dfs(i, level):
            if (level >= n):
                res.append(board.copy())
                return
            
            if (i < n and validPos(level, i, board)):
                board[level] = board[level][:i] + "Q" + board[level][i+1:]
                dfs(0, level + 1)
                board[level] = board[level][:i] + "." + board[level][i+1:]
            
            if (i < n):
                dfs(i + 1, level)

        def validPos(row, col, board):
            row_ind = 0
            while row_ind < n:
                if board[row_ind][col] == "Q" and row_ind != row:
                    return False
                row_ind += 1
            
            col_ind = 0
            while col_ind < n:
                if board[row][col_ind] == "Q" and col_ind != col:
                    return False
                col_ind += 1
                
            row_start = max(row - col, 0)
            col_start = max(col - row, 0)
            while (row_start < n and col_start < n):
                if (board[row_start][col_start] == "Q" and row_start != row and col_start != col):
                    return False
                row_start += 1
                col_start += 1

            row_end = max(row - (n - 1 - col), 0)
            col_end = min(row + col, n - 1)

            while (row_end < n and col_end >= 0):
                if (board[row_end][col_end] == "Q" and row_end != row and col_end != col):
                    return False
                row_end += 1
                col_end -= 1

            return True

        dfs(0, 0)
        return res
