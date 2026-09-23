class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_product = 0
        l, r = 0, len(heights) - 1
        while r > l and r >= 0 and l < len(heights):
            print(l, r)
            height1 = heights[l]
            height2 = heights[r]
            product = (r - l) * min(height1, height2)
            if product > max_product:
                max_product = product
            #move the minimum one
            if height1 < height2:
                l += 1
            else:
                r -= 1
        return max_product

        #what I asked LLMs:
        #a hint: starting r at the end instead -> insight, by doing this distance is already maximized
            
