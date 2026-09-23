class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        numsSum = sum(nums)
        
        # If the target is impossible to reach, return 0 early
        if abs(target) > numsSum:
            return 0
            
        # Size must be based on numsSum to accommodate all possible sums
        cache = [0] * (2 * numsSum + 1) 
        
        # Initial state: the last number can be added or subtracted
        # We use numsSum as the "zero" offset
        cache[numsSum - nums[-1]] += 1
        cache[numsSum + nums[-1]] += 1

        for i in range(len(nums) - 2, -1, -1):
            # tmp_cache must be the same size as cache
            tmp_cache = [0] * (2 * numsSum + 1)
            num = nums[i]
            for amt in range(len(cache)):
                if cache[amt] > 0:
                    # If we had ways to reach 'amt', we propagate those ways
                    if amt - num >= 0:
                        tmp_cache[amt - num] += cache[amt]
                    if amt + num < len(tmp_cache):
                        tmp_cache[amt + num] += cache[amt]
            cache = tmp_cache
            
        return cache[numsSum + target]