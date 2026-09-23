class Solution:
    def solve(self, board: List[List[str]]) -> None:
        
        ROWS = len(board)
        COLS = len(board[0])

        def isEdge(i, j):
            if (i == 0 or i == ROWS - 1 or j == 0 or j == COLS - 1):
                return True
            return False

        def changeToXIfS(i, j):
            if isEdge(i, j):
                return

            q = deque()
            visited = set()
            q.append((i, j))
            visited.add((i, j))
            dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]
            while q:
                r, c = q.popleft()
                for d in dirs:
                    nr, nc = r + d[0], c + d[1]
                    if (nr >= 0 and nr < ROWS 
                        and nc >= 0 and nc < COLS
                        and board[nr][nc] == 'O'
                        and (nr, nc) not in visited):
                        q.append((nr, nc))
                        visited.add((nr, nc))

                        if isEdge(nr, nc):
                            return

            for (i, j) in visited:
                board[i][j] = 'X'

        for i in range(ROWS):
            for j in range(COLS):
                if board[i][j] == 'O':
                    changeToXIfS(i, j)