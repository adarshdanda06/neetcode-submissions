class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ans = 0
        def backtrack(r, c):
            if r >= len(grid) or c >= len(grid[0]) or min(r, c) < 0 or grid[r][c] == 0:
                return 0
            
            grid[r][c] = 0
            return 1 + backtrack(r + 1, c) + backtrack(r - 1, c) + backtrack(r, c + 1) + backtrack(r,c - 1)
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (grid[i][j] == 1):
                    ans = max(ans, backtrack(i,j))
        return ans

        