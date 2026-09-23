class Solution:
    def climbStairs(self, n: int) -> int:

        def climb(current):
            if (current) > n:
                return 0
            if (current == n):
                return 1
            return climb(current + 1) + climb(current + 2)

        return climb(0)