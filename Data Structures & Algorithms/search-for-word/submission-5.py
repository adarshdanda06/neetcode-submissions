class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = []
        for i in range(len(board)):
            arr = []
            for j in range(len(board[0])):
                arr.append(False)
            visited.append(arr)

        def backtrack(row, col, rem):

            if row < 0 or row >= len(board) or col < 0 or col >= len(board[0]):
                return False

            if visited[row][col] == True or board[row][col] != rem[0]:
                return False
            
            if (board[row][col] == rem[0]):
                visited[row][col] = True
                if (len(rem) == 1):
                    return True
            result = backtrack(row + 1, col, rem[1:]) or backtrack(row - 1, col, rem[1:]) or backtrack(row, col + 1, rem[1:]) or backtrack(row, col - 1, rem[1:])
            visited[row][col] = not visited[row][col]
            return result

        for i in range(len(board) * len(board[0])):
            row = i // len(board[0])
            col = i % len(board[0])
            if backtrack(row, col, word) == True:
                return True
            
        return False







