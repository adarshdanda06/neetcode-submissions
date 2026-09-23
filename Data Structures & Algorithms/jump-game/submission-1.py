class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        #base case solution, if i == len(nums) - 1 -> we good
        n = len(nums)
        if (n == 1):
            return True
        cur_goal = n - 1

        i = n - 2
        while (i >= 0):
            if i + nums[i] >= cur_goal:
                cur_goal = i
                i = cur_goal - 1
            else:
                i -= 1
            if cur_goal == 0:
                return True
        return False
            