class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        #calculating target for each array
        total = 0
        for num in nums:
            total += num
        if total % 2 == 1:
            return False
        
        target = total / 2

        #lets say target it 15 for [1, 3, 4, 5, 7, 10]
        [3, 10, 1, 5, 7, 4]
        sum1 = 3, 13, 14, 19, 21, 18, 
        #do I check every possible subset, 
        #and see if there are 2 that make target: no because if one is -> the other automatically is

        memoization = {}
        def recurse(cur_sum, i):
            if (cur_sum, i) in memoization:
                return memoization[cur_sum, i]
            if cur_sum == target:
                memoization[cur_sum, i] = True
                return True
            if i >= len(nums):
                memoization[cur_sum, i] = False
                return False
            


            memoization[cur_sum, i] =  recurse(cur_sum, i + 1) or recurse(cur_sum + nums[i], i + 1)
            return memoization[cur_sum, i]
            
        return recurse(0, 0)
            




        #asking ai what:
        #should you sort the array: no