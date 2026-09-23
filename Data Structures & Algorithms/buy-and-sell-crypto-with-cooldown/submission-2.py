class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        prof = 0
        dp = {}


        def dfs(i, hasCoin):
            if i >= len(prices):
                return 0
            maxVal = 0

            if hasCoin: # sell
                val = prices[i] + dfs(i + 2, not hasCoin)
                maxVal = max(val, maxVal)
            else:
                val = dfs(i + 1, not hasCoin) - prices[i]
                maxVal = max(val, maxVal)

            maxVal = max(dfs(i + 1, hasCoin), maxVal) # do nothing

            return maxVal

        return dfs(0, False)


