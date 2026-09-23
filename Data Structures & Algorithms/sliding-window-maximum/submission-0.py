class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        stack = deque()

        l, r = 0, 0
        while (r < len(nums)):
            while (stack and nums[r] > stack[-1][0]):
                stack.pop()
            stack.append((nums[r], r))

            if (r - l + 1 == k):
                res.append(stack[0][0])
                if (stack[0][1] == l):
                    stack.popleft()
                l += 1
            r += 1

        return res