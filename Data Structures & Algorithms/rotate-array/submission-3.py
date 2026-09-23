class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # [7, 8, 9, 4, 5, 6, 1, 2, 3]
        # 4, 7
        def reverse(start, end):
            mid = (start + end) // 2
            negInd = 0
            for i in range(start, mid + 1):
                temp = nums[i]
                nums[i] = nums[end-negInd]
                nums[end-negInd] = temp
                negInd += 1


        k = k % len(nums)
        reverse(0, len(nums) - 1)
        reverse(0, k - 1)
        reverse(k, len(nums) - 1)

