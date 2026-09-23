class Solution:
    def jump(self, nums: List[int]) -> int:
        reach = 0
        end = 0
        jumpCount = -1

        for i, num in enumerate(nums):
            reach = max(reach, i + nums[i])

            if i == end:
                jumpCount += 1
                end = min(reach, len(nums) - 1)

        return jumpCount




