class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        part = 0
        for i in range(len(nums)):
            if (nums[i] == 0):
                nums[i], nums[part] = nums[part], nums[i]
                part += 1

        for i in range(part, len(nums)):
            if (nums[i] == 1):
                nums[i], nums[part] = nums[part], nums[i]
                part += 1

        