class Solution:
    from collections import defaultdict
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #two pointers and a hash_map
        ans = set()
        hash_map = defaultdict(int)
        for i in nums:
            hash_map[i] += 1
        
        r = 0

        while r < len(nums) - 2:
            l = r + 1
            while l < len(nums) - 1:
                find = 0 - (nums[r] + nums[l])
                hash_map[nums[r]] -= 1
                hash_map[nums[l]] -= 1
                
                if find in hash_map and hash_map[find] > 0:
                    numbs = [find, nums[r], nums[l]]
                    
                    numbs = tuple(sorted(numbs))
                    print(numbs)
                    ans.add(numbs)
                hash_map[nums[r]] += 1
                hash_map[nums[l]] += 1
                l += 1
            r += 1
        
        final_ans = []
        for lists in ans:
            final_ans.append(list(lists))
        return final_ans
