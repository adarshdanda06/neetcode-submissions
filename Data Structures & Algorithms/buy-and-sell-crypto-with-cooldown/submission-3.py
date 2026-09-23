class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = {}

        def dfs(i, hasCoin):
            if i >= len(prices):
                return 0

            if (i, hasCoin) in dp:
                return dp[(i, hasCoin)]

            maxVal = dfs(i + 1, hasCoin)
            if hasCoin:
                val = prices[i] + dfs(i + 2, not hasCoin)
                dp[(i, hasCoin)] = max(val, maxVal)

            else:
                val = dfs(i + 1, not hasCoin) - prices[i]
                dp[(i, hasCoin)] = max(val, maxVal)

            return dp[(i, hasCoin)]

        return dfs(0, False)