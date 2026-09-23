class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = []
        total_count = 0
        for i in range(len(grid)):
            vis_cur = [False for _ in range(len(grid[0]))]
            visited.append(vis_cur)
        #count number of islands
        def backtrack(r, c):
            if r == len(grid) or c == len(grid[0]) or min(r, c) < 0 or grid[r][c] == '0':
                return 
            
            grid[r][c] = '0'
            backtrack(r + 1, c)
            backtrack(r - 1, c)
            backtrack(r, c + 1)
            backtrack(r, c - 1)


            
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == '1':
                    backtrack(r, c)
                    total_count += 1
                
        return total_count
        


        