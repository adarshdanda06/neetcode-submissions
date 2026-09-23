

class Solution:
    def rob(self, nums: List[int]) -> int:
        '''
        memoize = {}
        def recurse(i):
            if i >= len(nums):
                return 0
            if i in memoize:
                return memoize[i]
            memoize[i] = max(nums[i] + recurse(i + 2), recurse(i + 1))
            return memoize[i]
        return recurse(0) '''

        #let's do bottom up approach: need recent stuff
        if len(nums) == 1:
            return nums[0]
        total_cost = [nums[0], max(nums[0], nums[1])]
        for i in range(2, len(nums)):
            new = nums[i] + total_cost[0]
            new = max(new, total_cost[1])
            total_cost = [total_cost[1], new]
        
        return total_cost[1]

            





        

