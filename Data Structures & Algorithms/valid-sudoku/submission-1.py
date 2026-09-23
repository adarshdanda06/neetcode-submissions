class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        lenRow = []
        lenCol = []
        lenBox = []
        for i in range(len(board)):
            for j in range(len(board[i])):
                if (board[i][j] != '.'):
                    lenRow.append(board[i][j])
                if (board[j][i] != '.'):
                    lenCol.append(board[j][i])
                if (board[3 * (i // 3) + (j // 3)][(3 * (i % 3)) + (j % 3)] != '.'):
                    lenBox.append(board[3 * (i // 3) + (j // 3)][(3 * (i % 3)) + (j % 3)])

            if (len(lenRow) != len(set(lenRow)) or len(lenCol) != len(set(lenCol)) or len(lenBox) != len(set(lenBox))):
                return False

            lenRow, lenCol, lenBox = [], [], []

        return True