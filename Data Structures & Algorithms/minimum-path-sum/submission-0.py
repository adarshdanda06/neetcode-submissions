class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        memo = {}
        def dfs(row, col):
            if (row, col) in memo:
                return memo[(row, col)]
            if row == len(grid) - 1 and col == len(grid[0]) - 1:
                return grid[-1][-1]
            if row >= len(grid):
                return float('inf')
            if col >= len(grid[0]):
                return float('inf')
            
            res = grid[row][col] + min(dfs(row + 1, col), dfs(row, col + 1))
            memo[(row, col)] = res
            return res

        return dfs(0, 0)
            
