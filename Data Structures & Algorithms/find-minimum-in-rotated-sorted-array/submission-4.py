class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        curr_min = min(nums[l], nums[r])
        if (nums[l] < nums[r]):
            return nums[l]
        while (l < r):
            m = (l + r) // 2
            if (nums[l] > nums[m]):
                r = m
            elif (nums[m] > nums[l]):
                l = m
            else:
                l += 1

        return nums[r]