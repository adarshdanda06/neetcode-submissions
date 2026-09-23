class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}

        def recurse(tot):
            if tot == n:
                return 1
            if tot > n:
                return 0

            if tot in memo:
                return memo[tot]            

            memo[tot] = recurse(tot + 1) + recurse(tot + 2) 
            return memo[tot]       
        return recurse(0)