class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        dp = [cost[0], cost[1]]
        for r in range(2, len(cost)):
            tmp = dp[1]
            dp[1] = cost[r] + min(dp[0], dp[1])
            dp[0] = tmp

        return min(dp[0], dp[1])