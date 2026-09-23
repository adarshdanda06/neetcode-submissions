

class Solution:
    def rob(self, nums: List[int]) -> int:
        memoization = {}
        def recurse(i):
            if i >= len(nums):
                return 0
            if i not in memoization:
                memoization[i] = max(nums[i] + recurse(i + 2),recurse(i + 1))
            
            return memoization[i]
            

        return recurse(0)
                

        

