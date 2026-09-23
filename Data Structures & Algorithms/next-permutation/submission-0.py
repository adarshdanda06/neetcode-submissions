class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        

    # [3, 2, 1]

    # [1, 2, 3]
    # backward thru the arr -> prev elem, less than the next elem
    # swap there

    # [1, 3, 2]
    # [2, 1, 3]
    
    #              
    # [1, 3, 2, 5, 4]
    # while going back, get the minimum val after i
        # min is 3

    # swap min and curr ind
    # go thru i + 1 and the end, then reverse
    

    # go back thru the array starting at len(nums) - 1
    #   accumulate the min as we go backward for i + 1
    #   when we reach a number that is less than i + 1, 
        #  two pointer approach
        #       # swap val at pointer, and push pointers close to each other

    # 
    #  i
    #        l  r 
    # [1, 3, 2, 0]
             
    # [1, 3, 2, 4]
    # [2, 4, 3, 1]
        descending = True
        for ind in range(len(nums) - 1):
            if nums[ind] < nums[ind + 1]:
                descending = False

        if descending:
            l = 0
            r = len(nums) - 1
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                r -= 1
                l += 1

            return

        for ind in range(len(nums) - 2, -1, -1):
            current_val = nums[ind]
            next_val = nums[ind + 1]
            if (current_val < next_val):
                min_val_greater_curr = next_val 
                min_ind = ind + 1

                for i in range(ind + 2, len(nums)):
                    if nums[i] > current_val:
                        min_val_greater_curr = min(nums[i], min_val_greater_curr)
                        min_ind = i

                nums[ind], nums[min_ind] = min_val_greater_curr, current_val

                l = ind + 1
                r = len(nums) - 1
                while l < r:
                    nums[l], nums[r] = nums[r], nums[l]
                    r -= 1
                    l += 1

                break
        return 

    # [1, 4, 3, 2]

    # [1, 3, 2, 4]


    # [1, 3, 2]

    #.    i
    # [2, 3, 1]

    #  

    # [2, 4, 1, 3]


    # [2, 1, 4, 3]






