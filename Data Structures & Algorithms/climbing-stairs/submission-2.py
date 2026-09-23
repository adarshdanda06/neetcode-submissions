class Solution:
    def climbStairs(self, n: int) -> int:
        cache = {}
        def climb(current, cache):
            if (current) >= n:
                return current == n
            cache[current] = climb(current + 1, cache) + climb(current + 2, cache)
            return cache[current]

        return climb(0, cache)