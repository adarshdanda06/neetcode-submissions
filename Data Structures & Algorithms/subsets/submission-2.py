class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = set()
        curr = []
        def dfs(i):
            nonlocal res
            nonlocal curr
            if i >= len(nums):
                return

            curr.append(nums[i])
            res.add(tuple(curr.copy()))
            dfs(i + 1)
            curr.pop()
            res.add(tuple(curr.copy()))
            dfs(i + 1)

        dfs(0)
        return [list(arr) for arr in res]
        
            


