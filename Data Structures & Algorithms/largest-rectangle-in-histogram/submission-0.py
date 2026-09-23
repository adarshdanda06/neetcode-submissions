class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        post = [len(heights)] * len(heights)
        post_tuple = []
        for i in range(len(heights)):
            while post_tuple and heights[i] < post_tuple[-1][0]:
                height, ind = post_tuple.pop()
                post[ind] = i
            post_tuple.append([heights[i], i])

        pre = [-1] * len(heights)
        pre_tuple = []
        for i in range(len(heights) - 1, -1, -1):
            while pre_tuple and heights[i] < pre_tuple[-1][0]:
                height, ind = pre_tuple.pop()
                pre[ind] = i
            pre_tuple.append([heights[i], i])

        max_val = 0
        print("Post: ", post)

        print("Pre: ", pre)


        for i in range(len(heights)):
            max_val = max(heights[i] * (post[i] - pre[i] - 1), max_val)

        return max_val            