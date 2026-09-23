class Solution:
    def climbStairs(self, n: int) -> int:

        def dfs(i, cache):
            if i in cache:
                return cache[i]

            if i == 1 or i == 2:
                return i

            cache[i] = dfs(i - 1, cache) + dfs(i - 2, cache)
            return cache[i]

        return dfs(n, {})