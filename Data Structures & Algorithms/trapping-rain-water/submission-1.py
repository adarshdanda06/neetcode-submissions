class Solution:
    def trap(self, height: List[int]) -> int:
        tot = 0
        l, r = 0, len(height) - 1
        leftMax, rightMax = height[l], height[r]
        while (l < r):
            if (leftMax < rightMax):                    
                l += 1
                leftMax = max(leftMax, height[l])
                tot += leftMax - height[l]
            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                tot += rightMax - height[r]
        return tot