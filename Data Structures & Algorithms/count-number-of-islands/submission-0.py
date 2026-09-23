class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        visited = set()
        def search(r, c):
            if r >= 0 and r < len(grid) and c >= 0 and c < len(grid[0]) and grid[r][c] == '1' and (r, c) not in visited:
                visited.add((r, c))
                search(r, c + 1)
                search(r, c - 1)
                search(r + 1, c)
                search(r - 1, c)
            else:
                return

        count = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == '1' and (r, c) not in visited:
                    count += 1
                    search(r, c)

        return count