class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        #lets do memoization approach first
        '''
        memoization = {}
        def recurse(i):
            if i >= len(cost):
                return 0
            if i in memoization:
                return memoization[i]

            memoization[i] = min(cost[i] + recurse(i + 1), cost[i] + recurse(i + 2))
            return memoization[i]
        return min(recurse(0), recurse(1)) '''

        #bottom up
        price_arr = []
        price_arr.append(cost[0])
        price_arr.append(cost[1])
        for i in range(2, len(cost)):
            price_arr.append(cost[i] + min(price_arr[i - 1], price_arr[i - 2]))

        return min(price_arr[len(cost) - 1], price_arr[len(cost) - 2])

