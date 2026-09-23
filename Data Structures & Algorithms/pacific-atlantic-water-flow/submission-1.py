class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        pacific = [[False for _ in range(COLS)] for _ in range(ROWS)]
        atlantic = [[False for _ in range(COLS)] for _ in range(ROWS)]
        pq = deque()
        aq = deque()
     
        for i in range(ROWS):
            pacific[i][0] = True
            pq.append((i, 0))
            atlantic[i][COLS - 1] = True
            aq.append((i, COLS - 1))

        for c in range(COLS):
            pacific[0][c] = True
            atlantic[ROWS - 1][c] = True
            pq.append((0, c))
            aq.append((ROWS - 1, c))

        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        def bfs(matrix, q):
            while q:
                r, c = q.popleft()
                for d in dirs:
                    nr, nc = r + d[0], c + d[1]
                    if (nr >= 0 and nr <= ROWS - 1
                        and nc >= 0 and nc <= COLS - 1
                        and not matrix[nr][nc]
                        and heights[nr][nc] >= heights[r][c]):
                            matrix[nr][nc] = True
                            q.append((nr, nc))

        bfs(pacific, pq)
        bfs(atlantic, aq)
        res = []

        for i in range(ROWS):
            for j in range(COLS):
                if pacific[i][j] and atlantic[i][j]:
                    res.append([i, j])

        return res
    