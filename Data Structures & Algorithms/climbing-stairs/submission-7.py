class Solution:
    def climbStairs(self, n: int) -> int:
        ways = [1, 2]
        if n <=2:
            return ways[n - 1]

        for i in range(3, n + 1):
            new_one = ways[0] + ways[1]
            ways = [ways[1], new_one]
        return  ways[1]