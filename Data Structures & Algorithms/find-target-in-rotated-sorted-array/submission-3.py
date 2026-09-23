class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # calculate mid
        # case 1, if mid == target

        # l       m       r
        # 4 5 6 7 8 9 1 2 3 
        
        # m
        # l.r
        # 7 0 1 2 3 4
        
        # l       l m r
        # 7 8 9 1 2 3 4

        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return m
            # case 2
            # if mid is on left side of pivot

            if nums[m] > nums[r]:
                # if target > nums[m]:
                #    l = m + 1
                if target < nums[m] and target >= nums[l]:
                    r = m - 1      
                else:
                    l = m + 1

            # case 3
            # if mid is on right side of piv
            else: # m < r
                # if target < nums[m]:
                #    r = m - 1
                if target > nums[m] and target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1

                
        return -1


    

        


            

        