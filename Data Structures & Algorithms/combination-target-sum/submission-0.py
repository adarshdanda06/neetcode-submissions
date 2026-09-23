class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()

        res = []
        curr = []

        def dfs():
            if (sum(curr) > target):
                return
            if (sum(curr) == target):
                if (sorted(curr) not in res):
                    res.append(sorted(curr))
                return

            for i in range(len(nums)):
                curr.append(nums[i])
                dfs()
                curr.pop()

        dfs()
        return res