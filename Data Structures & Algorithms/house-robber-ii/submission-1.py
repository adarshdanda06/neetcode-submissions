class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        first, second = 0, 0
        for i in range(len(nums) - 1):
            curr = first + nums[i]
            first = second
            second = max(curr, second)

        f, s = 0, 0
        for i in range(1, len(nums)):
            curr = f + nums[i]
            f = s
            s = max(curr, s)

        return max(first, second, f, s)