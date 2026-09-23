class Solution:
    def canJump(self, nums: List[int]) -> bool:
        reach = nums[0]
        for i in range(1, len(nums)):
            if reach < i:
                return False

            reach = max(reach, i + nums[i])
        
        return reach >= len(nums) - 1
      # farthest:
      # 1, 
      # if currInd < furthest, ret false
      