class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        picked = [False] * len(nums)
        count = 0
        res = []
        curr = []

        def dfs(count, picked_arr):
            if count >= len(nums):
                res.append(curr.copy())
                return

            for i in range(len(nums)):
                if not picked_arr[i]:
                    curr.append(nums[i])
                    picked_arr[i] = True
                    dfs(count + 1, picked_arr)
                    picked_arr[i] = False
                    curr.pop()


        dfs(0, picked)
        return res
