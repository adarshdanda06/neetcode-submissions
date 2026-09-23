class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # [7, 8, 9, 4, 5, 6, 1, 2, 3]
        # 4, 7
        def reverse(start, end):
            print(start)
            print(end)
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

    

        # [1, 2, 3, 4, 5, 6, 7, 8, 9] , k = 3

        # [7, 8, 9, 3, 2, 1, 6, 5, 4]
        # [7, 8, 9, 1, 2, 3, 6, 5, 4]
        # [7, 8, 9, 1, 2, 3, 4, 5, 6]

        # [7, 8, 9, 1, 2, 3, 4, 5, 6]




        # [2, 5, 6, 8, 9, 10, 11, 12, 13, 14], k = 2
        # [13, 14, 6, 8, 9, 10, 11, 12, 2, 5]
        # [13, 14, 5, 2, 12, 11, 10, 9, 8, 6]
        # [13, 14, 2, 5, 6, 8, 9, 10, 11, 12]

        # [13, 14, 2, 5, 6, 8, 9, 10, 11, 12]


