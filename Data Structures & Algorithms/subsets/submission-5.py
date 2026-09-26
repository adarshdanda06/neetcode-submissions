class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        curr = []
        def dfs(i):
            nonlocal curr
            if i >= len(nums):
                res.append(curr.copy())
                return

            # include curr
            curr.append(nums[i])
            dfs(i + 1)
            curr.pop()

            dfs(i + 1)
            # dont include curr

        dfs(0)
        return res
        
