class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        dp = [0, 0, nums[0]]
        for r in range(1, len(nums)):
            tmp = nums[r] + max(dp[0], dp[1])
            dp[2], dp[1], dp[0] = tmp, dp[2], dp[1]

        return max(dp[1], dp[2])