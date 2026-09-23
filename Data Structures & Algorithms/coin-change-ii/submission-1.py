class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = {}
        
        # repeated work when we get same i and same total -> can cache this
        def dfs(i, total):
            if total < 0:
                return 0
            if total == 0:
                return 1

            if (i, total) in dp:
                return dp[(i, total)]
            totalPaths = 0
            for ind in range(i, len(coins)):
                coin = coins[ind]
                totalPaths += dfs(ind, total - coin)
            dp[(i, total)] = totalPaths
            return totalPaths

        return dfs(0, amount)
                               # 4
 
                  # 3                         2. 1

        # 2        1.         0              0
 
    #  1  0 -1    -1 -2       -2

# 0 -1 -2