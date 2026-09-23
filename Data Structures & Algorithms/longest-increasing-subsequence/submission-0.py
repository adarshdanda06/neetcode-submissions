class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        max_sub = 0
        count = 0
        def dfs(i, prev):
            nonlocal count, max_sub

            for j in range(i, len(nums)):
                if nums[j] > prev:
                    count += 1
                    max_sub = max(count, max_sub)
                    dfs(j + 1, nums[j])
                    count -= 1
        dfs(0, float('-inf'))    

        return max_sub


            