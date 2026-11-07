class Solution:
    def minOperations(self, nums: List[int]) -> int:
        ans = 0

        for r in range(len(nums) - 2):
            if (nums[r] == 0):
                for i in range(r, r + 3):
                    nums[i] ^= 1
                ans += 1

        return ans if nums[-2] == 1 and nums[-1] == 1 else -1