class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        def helper(i, arr):
            if (i >= len(nums)):
                ans.append(arr[:])
                return
            cur = nums[i]
            arr.append(cur)
            helper(i + 1, arr)
            arr.pop()
            while (i + 1) < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            helper(i + 1, arr)
        
        helper(0, [])
        return ans