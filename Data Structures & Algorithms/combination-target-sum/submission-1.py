class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        curr = []

        def dfs(i, val):
            if (val == target):
                res.append(curr.copy())
                return
            if (i >= len(nums) or val > target):
                return
            curr.append(nums[i])
            val += nums[i]
            dfs(i, val)
            val -= nums[i]
            curr.pop()

            dfs(i + 1, val)
        
        dfs(0, 0)
        return res

