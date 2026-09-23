class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        low, high, res = nums[0], nums[0], nums[0]
        for i in range(1, len(nums)):
            res1 = high * nums[i]
            res2 = low * nums[i]

            low = min(nums[i], res2, res1)
            high = max(nums[i], res2, res1)

            res = max(res, high)

        return res

            
