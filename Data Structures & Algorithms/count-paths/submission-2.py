class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memoization = []
        for i in range(m):
            ans = []
            for j in range(n):
                ans.append(-1)
            memoization.append(ans)
            
        def recurse(r, c):
            if r == m or c == n:
                return 0
            if r == m - 1 and c == n - 1:
                memoization[r][c] = 1
                return 1
            if memoization[r][c] != -1:
                return memoization[r][c]

            memoization[r][c] = recurse(r + 1, c) + recurse(r, c + 1)
            return memoization[r][c]
        return recurse(0, 0)