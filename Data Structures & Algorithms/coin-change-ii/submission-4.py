class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        memo = [0 for i in range(amount + 1)]
        memo[0] = 1

        # 4 is amount
        # 5 is col len
        # [0, 0, 0, 0, 1]

        #  [1, 1, 2, 3, 4, 5], 1
        #  [1, 0, 1, 1, 1, 1], 2
        #  [1, 0, 0, 1, 0, 0]. 3

        # [1, 1, 2, 3, 4, 5] 1

        # 1, 2, 3

        # 1 1 1 1 1
        # 1 1 1 2
        # 1 1 3
        # 2 2 1
        # 2 3

        for coinInd in range(len(coins) - 1, -1, -1):
            for amountVal in range(1, len(memo)):
                prevAmount = amountVal - coins[coinInd]
                if prevAmount < 0:
                    continue

                numOfWays = memo[amountVal] + memo[prevAmount]
                memo[amountVal] = numOfWays

        return memo[-1]

                

            

            

        # repeated work when we get same i and same total -> can cache this

                               # 4
 
                  # 3                         2. 1

        # 2        1.         0              0
 
    #  1  0 -1    -1 -2       -2

# 0 -1 -2