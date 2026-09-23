class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        numsSum = sum(nums)

        if abs(target) > numsSum:
            return 0

        cache = [0] * (2 * numsSum + 1)
        lastNum = nums[-1]
        cache[numsSum - lastNum] += 1
        cache[numsSum + lastNum] += 1

        for i in range(len(nums) - 2, -1, -1):
            tmp_cache = [0] * (2 * numsSum + 1)
            num = nums[i]
            for amt in range(len(tmp_cache)):
                if amt - num >= 0:
                    tmp_cache[amt] += cache[amt - num]
                if amt + num < len(tmp_cache):
                    tmp_cache[amt] += cache[amt + num]

            cache = tmp_cache
        return cache[numsSum + target]

