class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        # all dest nodes 
        def inbounds(i, j):
            if i < 0 or i >= len(matrix) or j < 0 or j >= len(matrix[0]):
                return False
            return True
        

        # [7, 7, 5]
        # [2, 4, 6]
        # [8, 2, 0]
        cache = {}
        def dfs(i, j, val):
            if (i, j, val) in cache:
                return cache[(i, j, val)]

            if not inbounds(i, j):
                return 0

            if matrix[i][j] <= val:
                return 0

            dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
            maxDepth = 0
            for r, c in dirs:
                newRow = r + i
                newCol = c + j
                dist = 1 + dfs(newRow, newCol, matrix[i][j])
                maxDepth = max(dist, maxDepth)

            cache[(i, j, val)] = maxDepth
            return maxDepth

        maxVal = 0
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                maxVal = max(dfs(r, c, -1), maxVal)

        return maxVal



        

