class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = -1001
        cur_sum = -1001
        for num in nums:
            if num > cur_sum + num:
                cur_sum = num
            else:
                cur_sum += num
            max_sum = max(max_sum, cur_sum)
        return max_sum

        