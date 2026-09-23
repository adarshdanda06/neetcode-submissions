class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        prof = 0

        def dfs(i, hasCoin):
            if i >= len(prices):
                return 0

            maxVal = dfs(i + 1, hasCoin) # do nothing
            if hasCoin: # sell
                val = prices[i] + dfs(i + 2, False)
                maxVal = max(val, maxVal)
            else:
                val = dfs(i + 1, True) - prices[i]
                maxVal = max(val, maxVal)

            return maxVal

        return dfs(0, False)


