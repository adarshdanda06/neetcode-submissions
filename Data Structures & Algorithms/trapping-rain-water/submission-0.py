class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        l_max_ind = 0
        r_max_ind = len(height) - 1
        tot = 0
        while (l < r):
            if (height[l] <= height[r]):
                l += 1
                l_max_ind = l if height[l] > height[l_max_ind] else l_max_ind
                while (height[l] < height[l_max_ind]):
                    tot += height[l_max_ind] - height[l]
                    l += 1
                    l_max_ind = l if height[l] > height[l_max_ind] else l_max_ind

            else:
                r -= 1
                r_max_ind = r if height[r] > height[r_max_ind] else r_max_ind
                while (height[r] < height[r_max_ind]):
                    tot += height[r_max_ind] - height[r]
                    r -= 1
                    r_max_ind = r if height[r] > height[r_max_ind] else r_max_ind


        return tot