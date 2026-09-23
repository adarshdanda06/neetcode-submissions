class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        sub_max = 0
        def dfs(i, prev, count):
            if i >= len(nums):
                return

            nonlocal sub_max
            if nums[i] > prev:
                sub_max = max(count, sub_max)
                dfs(i + 1, nums[i], count + 1)

            dfs(i + 1, prev, count)

        dfs(0, float('-inf'), 1)
        return sub_max
            

            