class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}

        def recurse(rem):
            if rem == 0:
                return 1
            if rem < 0:
                return 0
            if rem in memo:
                return memo[rem]            

            memo[rem] = recurse(rem - 1) + recurse(rem - 2) 
            return memo[rem]       
        return recurse(n)