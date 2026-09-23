class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        cache = [0] * len(nums)
        res = 1

        for i in range(len(nums) - 1, -1, -1):
            cache[i] = 1
            for j in range(i + 1, len(nums)):
                if nums[j] > nums[i]:
                    cache[i] = max(cache[i], 1 + cache[j])
                    res = max(cache[i], res)

        return res

        

            

            