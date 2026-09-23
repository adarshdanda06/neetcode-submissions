class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        curr = []

        def dfs(i, tot):
            if (tot == target):
                res.append(curr.copy())
                return
            if (i >= len(nums) or tot > target):
                return
            curr.append(nums[i])
            dfs(i, tot + nums[i])
            curr.pop()

            dfs(i + 1, tot)
        
        dfs(0, 0)
        return res

