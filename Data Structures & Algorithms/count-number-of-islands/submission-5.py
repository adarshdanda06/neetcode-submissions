class Solution:
    from collections import deque
    def numIslands(self, grid: List[List[str]]) -> int:
        ans = 0
        visited = set()
        queue = deque()
        def bfs(i, j):
            queue.append((i, j))
            visited.add((i, j))
            while queue:
                i, j = queue.popleft()
                
                if i + 1 < len(grid) and grid[i + 1][j] == '1' and (i + 1, j) not in visited:
                    queue.append((i + 1, j))
                    visited.add((i + 1, j))
                
                if j + 1 < len(grid[0]) and grid[i][j + 1] == '1' and (i, j + 1) not in visited:
                    queue.append((i, j + 1))
                    visited.add((i, j + 1))
                
                if i - 1 > -1 and grid[i - 1][j] == '1' and (i - 1, j) not in visited:
                    queue.append((i - 1, j))
                    visited.add((i - 1, j))

                if j - 1 > -1 and grid[i][j - 1] == '1' and (i, j - 1) not in visited:
                    queue.append((i, j - 1))
                    visited.add((i, j - 1))

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1' and (i, j) not in visited:
                    bfs(i, j)
                    ans +=1
        
        return ans
            
       
        



