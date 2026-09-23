class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        MROWS = len(grid)
        MCOLS = len(grid[0])

        def inbounds(r, c):
            if r < 0 or r >= MROWS or c < 0 or c >= MCOLS:
                return False
            return True
        q = deque()
        visited = set()

        def bfs():
            while q:
                r, c = q.popleft()
                directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
                for d in directions:
                    nr = r + d[0]
                    nc = c + d[1]
                    if inbounds(nr, nc) and grid[nr][nc] != -1 and (nr, nc) not in visited:
                        grid[nr][nc] = grid[r][c] + 1
                        q.append((nr, nc))
                        visited.add((nr, nc))
    
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    q.append((i, j))
                    visited.add((i, j))

        bfs()




        