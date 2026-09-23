class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        val = nums[0]


        while (l <= r):
            if (nums[l] < nums[r]):
                val = min(val, nums[l])
                break

            m = (l + r) // 2
            if (nums[m] >= nums[l]):
                l = m + 1
            else:
                r = m - 1
            val = min(val, nums[m])

        return val