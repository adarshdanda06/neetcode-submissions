class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        count = 0
        def inRange(r, c):
            if r >= 0 and r < len(grid) and c >= 0 and c < len(grid[0]):
                return True

            return False

        def bfs(r, c):
            q = deque()
            directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

            q.append((r, c))

            while q:
                row, col = q.popleft()
                if inRange(row, col) and grid[row][col] == '1':
                    for d in directions:
                        newDir = (row + d[0], col + d[1])
                        if inRange(*newDir) and grid[newDir[0]][newDir[1]] == '1' and newDir not in visited:
                            visited.add(newDir)
                            q.append(newDir)

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if (r, c) not in visited and grid[r][c] == '1':
                    visited.add((r, c))
                    count += 1
                    bfs(r, c)

        return count