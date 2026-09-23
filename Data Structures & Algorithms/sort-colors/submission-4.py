class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        one, zero = 0, 0
        for i in range(len(nums)):
            tmp = nums[i]
            nums[i] = 2

            if tmp == 1 or tmp == 0:
                nums[one] = 1
                one += 1
            if tmp == 0:
                nums[zero] = 0
                zero += 1
