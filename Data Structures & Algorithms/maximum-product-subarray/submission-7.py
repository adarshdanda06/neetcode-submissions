class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxi, mini = nums[0], nums[0]
        cur_max, cur_min = nums[0], nums[0]

        for i in range(1, len(nums)):

            cur_num = nums[i]
            old_cur_max = cur_max
            cur_max = max(nums[i], cur_max * nums[i], cur_min * nums[i])
            cur_min = min(nums[i], old_cur_max * nums[i], cur_min * nums[i])
            if cur_max > maxi:
                maxi = cur_max
            if cur_min < mini:
                mini = cur_min
            print(maxi, mini, cur_max, cur_min)
        return maxi

        