class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        # [1, 2, 3, 4, 5, 6, 7, 8, 9] , k = 4
        # [6, 7, 8, 9, 1, 2, 3, 4, 5]

        for step in range(k):
            last = nums[-1]
            for i in range(len(nums) - 1, 0, -1):
                nums[i] = nums[i - 1]
            nums[0] = last


