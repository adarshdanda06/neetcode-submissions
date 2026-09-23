class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        height = len(nums)
        res = []
        curr = []
        def backtrack(depth):
            if (depth > height):
                return True

            if sorted(curr) not in res:
                res.append(sorted(curr))

            for i in range(len(nums)):
                if (nums[i] not in curr):
                    curr.append(nums[i])
                    backtrack(depth + 1)
                    curr.pop()
        
        backtrack(0)
        return res