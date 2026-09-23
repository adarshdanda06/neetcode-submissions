class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res, curr = [], []

        def dfs(ind, tot):
            if tot == target:
                res.append(curr.copy())
                return

            if tot > target:
                return

            for i in range(ind, len(nums)):
                curr.append(nums[i])
                dfs(i, tot + nums[i])
                curr.pop()

        dfs(0, 0)
        return res

        
            
