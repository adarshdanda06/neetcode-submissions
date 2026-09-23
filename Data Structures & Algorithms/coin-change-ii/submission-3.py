class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        memo = [[0 for i in range(amount + 1)] for j in range(len(coins))]
        
        for row in range(len(coins)):
            memo[row][0] = 1

        # 4 is amount
        # 5 is col len
        # [0, 0, 0, 0, 1]

        # []
        for row in range(len(memo) - 1, -1, -1):
            for col in range(1, len(memo[0])):
                currAmount = col
                total = 0
                for newR in range(row, len(coins)):
                    newAmount = currAmount - coins[newR]
                    if newAmount < 0:
                        continue
                    total += memo[newR][newAmount]

                memo[row][col] = total

        print(memo)
        return max([memo[i][len(memo[0]) - 1] for i in range(len(coins))])

        # repeated work when we get same i and same total -> can cache this

                               # 4
 
                  # 3                         2. 1

        # 2        1.         0              0
 
    #  1  0 -1    -1 -2       -2

# 0 -1 -2