class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        last = days[len(days) - 1]
        dp = [0] * (last + 1)
        days_set = set(days)

        for i in range(1, len(dp)):
            if i not in days_set:
                dp[i] = dp[i - 1]
                continue

            dp[i] = dp[i - 1] + costs[0]
            seven_ago = 0 if i - 7 < 0 else dp[i - 7]
            dp[i] = min(dp[i], seven_ago + costs[1])
            thir_ago = 0 if i - 30 < 0 else dp[i - 30]
            dp[i] = min(dp[i], thir_ago + costs[2])

        return dp[-1]