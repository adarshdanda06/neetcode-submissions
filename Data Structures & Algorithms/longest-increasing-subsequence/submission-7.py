class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        memoization = {}
        def recurse(i, prev):
            if (i, prev) in memoization:
                return memoization[i, prev]
            if i == len(nums):
                return 0
            memoization[i, prev] = recurse(i + 1, prev)
            if nums[i] > prev:

                memoization[i, prev] = max(1 + recurse(i + 1, nums[i]), memoization[i, prev])

            return memoization[i, prev]        
        return recurse(0, -1001)

        #brute force solution


        
    