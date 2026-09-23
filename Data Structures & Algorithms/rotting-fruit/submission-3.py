class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fruits = set()
        visited = set()
        q = deque()

        def inbounds(i, j):
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]):
                return False
            return True

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    continue
                elif grid[i][j] == 2:
                    visited.add((i, j))
                    q.append((i, j))

                fruits.add((i, j))

        res = 0
        dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        if q:
            res = -1
        while q:
            count = len(q)
            for num in range(count):
                r, c = q.popleft()

                for d in dirs:
                    nr, nc = r + d[0], c + d[1]
                    if inbounds(nr, nc) and (nr, nc) in fruits and (nr, nc) not in visited:
                        q.append((nr, nc))
                        visited.add((nr, nc))

            res += 1

        if visited != fruits:
            return -1
        return res
            