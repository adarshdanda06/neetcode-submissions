class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # 3 ptrs

        # keep track on ind while storing
        # sort in inc order
        #       i      l        r
        # [-4, -1, -1, 0, 0, 1, 2, 2]
        #   sum = -2
        #
        nums.sort()
        triplets = []

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            l = i + 1
            r = len(nums) - 1

            while l < r:
                sum_of_triplets = nums[i] + nums[r] + nums[l]

                if sum_of_triplets > 0:
                    r -= 1

                elif sum_of_triplets < 0:
                    l += 1

                else:
                    triplets.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1


        return triplets
        # for thru sorted nums
        #   l = i + 1
        #   r = len(nums) - 1
        #   while l < r:
            # sum_of_vals = nums[i] + nums[l] + nums[r]

        #   if sum of val < 0
            # l += 1

        #   if sum of vals > 0
            # dec r 

        # else:
            # add to set (val[i], val[l], val[r])

        

        # 

        # 
