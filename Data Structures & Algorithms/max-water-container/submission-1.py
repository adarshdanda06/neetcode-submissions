class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        maxVal = min(heights[l], heights[r]) * (r - l)
        while (l < r):
            if (heights[r] < heights[l]):
                r -= 1
            else:
                l += 1
            area = min(heights[r], heights[l]) * (r - l)
            maxVal = max(area, maxVal)
        return maxVal