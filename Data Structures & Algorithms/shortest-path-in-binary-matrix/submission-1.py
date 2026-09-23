from collections import deque
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if (grid[0][0] == 1):
            return -1

        length = 1
        queue = deque()
        visited = set()
        queue.append((0, 0))
        visited.add((0, 0))

        while queue:
            len_qu = len(queue)
            for i in range(len_qu):

                r, c = queue.popleft()
                if r == len(grid) - 1 and c == len(grid[0]) - 1:
                    return length
            
                neighbors = [[0, 1], [0, -1], [1, 0], [-1, 0], [1, 1], [1, -1], [-1, 1], [-1, -1]]
                for dr, dc in neighbors:
                    if min(r + dr, c + dc) < 0 or r + dr >= len(grid) or c + dc >= len(grid[0]) or grid[r + dr][c + dc] == 1 or  (r + dr, c + dc) in visited:
                        continue
                    visited.add((r + dr, c + dc))
                    queue.append((r + dr, c + dc))
            length += 1
        return -1




        