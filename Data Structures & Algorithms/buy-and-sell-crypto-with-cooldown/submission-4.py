class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        buy = [0] * (n + 2)
        sell = [0] * (n + 2)

        for i in range(n - 1, -1, -1):
            # buy side
            buyNow = -prices[i] + sell[i + 1]
            holdBuy = buy[i + 1]
            buy[i] = max(buyNow, holdBuy)

            sellNow = prices[i] + buy[i + 2]
            holdSell = sell[i + 1]
            sell[i] = max(sellNow, holdSell)

        return buy[0]

            # sell side