class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        time, fresh = 0, 0

        def inbounds(i, j):
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]):
                return False
            return True

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    fresh += 1
                elif grid[i][j] == 2:
                    q.append((i, j))

        dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        while q and fresh > 0:
            for i in range(len(q)):
                r, c = q.popleft()
                for d in dirs:
                    nr, nc = r + d[0], c + d[1]
                    if inbounds(nr, nc) and grid[nr][nc] == 1:
                        q.append((nr, nc))
                        grid[nr][nc] = 2
                        fresh -= 1

            time += 1
        return time if fresh == 0 else -1
            