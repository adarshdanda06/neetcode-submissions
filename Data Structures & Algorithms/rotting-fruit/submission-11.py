from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()
        visited = set()
        fresh = 0
        ans = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 2:
                    visited.add((row, col))
                    queue.append((row, col))
                elif grid[row][col] == 1:
                    fresh += 1
        neighbors = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        while queue and fresh != 0:
            ones_exist = False
            que_len = len(queue)
            for i in range(que_len):
                r, c = queue.popleft()
                for dr, dc in neighbors:
                    if min(r + dr, c + dc) < 0 or r + dr >= len(grid) or c + dc >= len(grid[0]) or grid[r + dr][c + dc] == 2 or (r + dr, c + dc) in visited:
                        continue
                    elif grid[r + dr][c + dc] == 1:
                        fresh -= 1
                        ones_exist = True
                        visited.add((r + dr, c + dc))
                        queue.append((r + dr, c + dc))
                        grid[r + dr][c + dc] = 2
            if ones_exist:
                ans += 1
        
        if fresh != 0:
            return -1
        return ans
            


                    



        


        