class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, maxProf = 0, 0
        for r in range(1, len(prices)):
            if (prices[r] < prices[l]):
                l = r
            maxProf = max(maxProf, prices[r] - prices[l])

        return maxProf