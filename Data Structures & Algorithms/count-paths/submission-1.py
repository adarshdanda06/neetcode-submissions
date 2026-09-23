class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        cache = [[-1 for _ in range(n)] for j in range(m)]
        
        def dfs(r, c):
            if r >= m or c >= n:
                return 0

            if r == m - 1 or c == n - 1:
                cache[r][c] = 1
                return 1
            
            if cache[r][c] == -1:
                cache[r][c] = dfs(r + 1, c) + dfs(r, c + 1)

            return cache[r][c]

        return dfs(0, 0)
        