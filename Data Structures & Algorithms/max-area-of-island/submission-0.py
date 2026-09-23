class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        visited = set()
        def search(row, col):
            queue = [(row, col)]
            count = 1
            while queue:
                val = queue.pop()
                
                for d in dirs:
                    curr = (val[0] + d[0], val[1] + d[1])
                    if curr[0] >= 0 and curr[0] < ROWS and curr[1] >= 0 and curr[1] < COLS and grid[curr[0]][curr[1]] == 1 and (curr[0], curr[1]) not in visited:
                        queue.append(curr)
                        visited.add(curr)
                        count += 1

            return count

        tot = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] not in visited and grid[r][c] == 1:
                    visited.add((r, c))
                    tot = max(search(r, c), tot)

        return tot
