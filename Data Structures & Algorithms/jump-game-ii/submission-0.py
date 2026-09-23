class Solution:
    def jump(self, nums: List[int]) -> int:
        #with each jump, want to get to furthest index
        i = 0
        jumpcount = 0
        furthest = 0
        current_end = 0
        for i in range(len(nums) - 1):
            furthest = max(furthest, i + nums[i])

            if i == current_end:
                current_end = furthest
                jumpcount += 1
        return jumpcount

        