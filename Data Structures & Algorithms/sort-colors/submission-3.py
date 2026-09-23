class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        one = 0
        zero = 0
        for i in range(len(nums)):
            if nums[i] == 1 and one == i:
                one += 1
                continue

            if nums[i] == 0 and zero == i:
                zero += 1
                one = max(zero, one)
                continue

            if nums[i] == 1:
                nums[one], nums[i] = nums[i], nums[one]
                one += 1
            
            elif nums[i] == 0:
                nums[zero], nums[i] = nums[i], nums[zero]
                val = nums[i]
                if val == 1:
                    nums[one], nums[i] = nums[i], nums[one]
                    one += 1
                zero += 1
                one = max(zero, one)

