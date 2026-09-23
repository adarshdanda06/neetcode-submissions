class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        list1 = [11 for _ in range(len(nums))]
        def helper(i, arr):
            if (i == len(nums)):
                ans.append(arr[:])
                return
            cur_num = nums[i]
            for ind in range(len(nums)):
                if (arr[ind] > 10):
                    arr[ind] = cur_num
                    helper(i + 1, arr)
                    arr[ind] = 11
        
        helper(0, list1)
        return ans