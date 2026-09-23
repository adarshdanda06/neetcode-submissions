class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        visited = []
        for i in range(len(grid)):
            visited_cur = [False for _ in range(len(grid[0]))]
            visited.append(visited_cur)
        def recurse(r, c):
            if ((r < 0 or c < 0) or (r == len(grid) or c == len(grid[0])) or visited[r][c] == True or grid[r][c] == 1):
                return 0
            if r == len(grid) - 1 and c == len(grid[0]) - 1:
                return 1
            visited[r][c] = True


            count = 0
            count += recurse(r + 1, c)
            count += recurse(r - 1, c)
            count += recurse(r, c + 1)
            count += recurse(r, c - 1)

            visited[r][c] = False
            return count
        return recurse(0, 0)

        