

class Solution:
    def rob(self, nums: List[int]) -> int:
        #want max amount
        #lets do memoization first
        memoize = {}
        def recurse(i):
            #if we rob house i, can't rob house i + 1
            #either we rob or don't rob
            if i >= len(nums):
                return 0
            if i in memoize:
                return memoize[i]
            memoize[i] = max(nums[i] + recurse(i + 2), recurse(i + 1))
            return memoize[i]
        return recurse(0)

        

