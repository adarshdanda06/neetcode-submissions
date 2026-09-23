class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        #2 choices: keep adding num, don't add num and move next
        ans = []
        def helper(i, arr, tot):
            if (i == len(nums) or tot > target):
                return
            
            if (tot == target):
                ans.append(arr[:])
                return
            cur = nums[i]
            arr.append(cur)
            helper(i, arr, tot + cur)
            arr.pop()
            helper(i + 1, arr, tot)
        
        helper(0, [], 0)
        return ans







        