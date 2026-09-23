class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = ["." * n] * n
        res = []
        col_set = set()
        pos_diag = set()
        neg_diag = set()

        def dfs(i, level):
            if (level >= n):
                res.append(board.copy())
                return
            
            for i in range(n):
                if i not in col_set and valid(level, i):
                    col_set.add(i)
                    pos_diag.add(i + level)
                    neg_diag.add(level - i)
                    board[level] = board[level][:i] + "Q" + board[level][i+1:]
                    dfs(0, level + 1)
                    board[level] = board[level][:i] + "." + board[level][i+1:]
                    col_set.remove(i)
                    pos_diag.remove(i + level)
                    neg_diag.remove(level - i)

        def valid(row, col):
            if row + col in pos_diag:
                return False
            if row - col in neg_diag:
                return False
            return True

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
