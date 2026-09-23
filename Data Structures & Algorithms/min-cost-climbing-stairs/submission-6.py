class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        #either go next or skip one
        [1, 2, 3]
        #lets do memoization approach first
        memoization = {}
        def recurse(i):
            if i >= len(cost):
                return 0
            if i in memoization:
                return memoization[i]

            memoization[i] = min(cost[i] + recurse(i + 1), cost[i] + recurse(i + 2))
            return memoization[i]
        return min(recurse(0), recurse(1))