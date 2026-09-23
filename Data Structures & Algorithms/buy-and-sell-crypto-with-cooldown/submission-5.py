class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memoization = []
        for i in range(len(prices)):
            memoization.append([-1, -1])
        def recurse(i, own):
            if i >= len(prices):
                return 0
            if memoization[i][own] != -1:
                return memoization[i][own]
\

            if own == True:

                memoization[i][1] = max(prices[i] + recurse(i + 2, False), recurse(i + 1, True))
                return memoization[i][1]
            else:
                memoization[i][0] = max(- 1 * prices[i] + recurse(i + 1, True), recurse(i + 1, False))
                return memoization[i][0] 

        return recurse(0, False)

        