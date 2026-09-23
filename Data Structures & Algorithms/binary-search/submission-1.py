class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, mid, r = 0, len(nums) // 2, len(nums) - 1
        while (l <= r):
            if (nums[mid] < target):
                l = mid + 1
                mid = (r + l) // 2 
            elif (nums[mid] > target):
                r = mid - 1
                mid = (r + l) // 2
            else:
                return mid


        return -1