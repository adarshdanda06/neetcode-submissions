class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = [[False for i in range(len(board[0]))] for j in range(len(board))]

        def inbounds(row, col):
            if row < 0 or row >= len(board) or col < 0 or col >= len(board[0]):
                return False
            return True

        def dfs(row, col, currentWord):
            if not inbounds(row, col):
                return False

            currentWord += board[row][col]
            if currentWord == word:
                return True

            lastIndex = len(currentWord) - 1
            if word[lastIndex] != currentWord[-1]:
                return False
        
            directions = [[0, 1], [0, -1], [-1, 0], [1, 0]]
            found_word = False

            for current_direction in directions:
                new_row  = row + current_direction[0]
                new_col = col + current_direction[1]

                if inbounds(new_row, new_col) and not visited[new_row][new_col]:
                    visited[new_row][new_col] = True
                    found_word = found_word or dfs(new_row, new_col, currentWord)
                    visited[new_row][new_col] = False

            return found_word

            
        for row in range(len(board)):
            for col in range(len(board[0])):
                current_char = board[row][col]
                if current_char == word[0]:
                    visited[row][col] = True
                    if dfs(row, col, ""):
                        return True

                    visited[row][col] = False

        return False
        # for thru board
            # run dfs on cell if the word starts with same word as in cell


        







