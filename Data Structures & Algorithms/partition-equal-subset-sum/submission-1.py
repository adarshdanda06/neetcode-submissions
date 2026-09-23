class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        tot = sum(nums)
        if (tot % 2 != 0):
            return False
        if len(nums) == 1:
            return False

        half = tot / 2
        nset = set()

        for i in range(len(nums)):
            curr_set = set()
            for item in nset:
                curr_set.add(item + nums[i])
            nset.add(nums[i])
            nset.update(curr_set)
            if half in nset:
                return True

        return False