class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        res = set()
        curr_set = set()
        curr = []

        def dfs(i):
            if len(curr_set) == len(nums):
                res.add(tuple(list(curr.copy())))
                return
            
            for i in range(len(nums)):
                num = nums[i]
                if num not in curr_set:
                    curr.append(num)
                    curr_set.add(num)
                    dfs(i)
                    curr.pop()
                    curr_set.remove(num)

        dfs(0)
        return [list(single) for single in res]