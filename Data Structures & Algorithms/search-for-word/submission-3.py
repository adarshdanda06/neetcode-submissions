class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def inbounds(row, col, board) -> bool:
            row_in = row >= 0 and row < len(board)
            col_in = col >= 0 and col < len(board[0])
            return row_in and col_in

        visited = set()

        def find(current, row, col):
            if (row, col) in visited or not inbounds(row, col, board) or len(current) > len(word):
                return False

            new_ind = len(current)

            if board[row][col] == word[new_ind]:
                current += board[row][col]
                if current == word:
                    return True
                visited.add((row, col))
                l = find(current, row, col - 1)
                r = find(current, row, col + 1)
                u = find(current, row - 1, col)
                d = find(current, row + 1, col)
                visited.remove((row, col))
                return l or r or u or d

            return False

        for row in range(len(board)):
            for col in range(len(board[0])):
                if (find("", row, col)):
                    return True
        return False

                    
