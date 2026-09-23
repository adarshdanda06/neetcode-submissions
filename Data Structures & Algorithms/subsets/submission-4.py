class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        total = []
        def helper(i, arr):
            if i == len(nums):
                total.append(arr[:])
                return

            cur = nums[i]
            arr.append(cur)
            helper(i + 1, arr)
            arr.pop()
            helper(i + 1, arr)
        helper(0, [])
        return total
        