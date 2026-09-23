class Solution:
    def rob(self, nums: List[int]) -> int:
        memoization = {}
        def recurse(i, numbers):
            if i >= len(numbers):
                return 0
            if i not in memoization:
                memoization[i] = max(numbers[i] + recurse(i + 2, numbers), recurse(i + 1, numbers))
            return memoization[i]
        if len(nums) == 1:
            return nums[0]
        ans1 = recurse(0, nums[1:])
        memoization.clear()
        ans2 = recurse(0, nums[:len(nums) - 1])
        return max(ans1, ans2)
        

            