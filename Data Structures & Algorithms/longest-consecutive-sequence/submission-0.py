class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        max_count = 0
        for i in range(len(nums)):
            count = 1
            if ((nums[i] + 1) not in num_set):
                curr = nums[i]
                while ((curr - 1) in num_set):
                    count += 1
                    curr -= 1
            max_count = max(max_count, count)
        return max_count