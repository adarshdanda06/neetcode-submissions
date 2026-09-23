class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        mins, fresh = 0, 0
        R = len(grid)
        C = len(grid[0])

        def inbounds(r, c):
            if r < 0 or r >= R or c < 0 or c >= C:
                return False
            return True


        for r in range(R):
            for c in range(C):
                if grid[r][c] == 2:
                    q.append((r, c))
                
                if grid[r][c] == 1:
                    fresh += 1
        print(fresh)
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        while q and fresh > 0:
            # go thr. values in the q
            # find neighbors for all, if valid add to q and fresh -= 1
            # add 1 to mins

            size = len(q)
            for i in range(size):
                r, c = q.popleft()


                for d in dirs:
                    nr = r + d[0]
                    nc = c + d[1]

                    if inbounds(nr, nc) and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        fresh -= 1
                        q.append((nr, nc))

            mins += 1

        print(fresh)
        return mins if fresh == 0 else -1


                
            