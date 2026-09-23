class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:


        # i, currSum
        # if i outbound:
            # ret 0

        # if i == len(nums) - 1 and currSUm = target:
            # return 1

        # choice 1: add nums[i] to currSum
        # choice 2: sub nums[i] from currSum

        def dfs(i, currSum):
            if i >= len(nums):
                if currSum == target:
                    return 1
                return 0

            add = dfs(i + 1, currSum + nums[i])
            sub = dfs(i + 1, currSum - nums[i])
            return add + sub

        return dfs(0, 0)

