class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        maxSum = 0
        prev = 0
        currSum = 0
        for i in range(len(nums)):
            if nums[i] > prev:
                currSum += nums[i]
                maxSum = max(currSum, maxSum)

            else:
                currSum = nums[i]
            prev = nums[i]

        return maxSum