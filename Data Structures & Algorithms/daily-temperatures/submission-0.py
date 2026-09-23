class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []

        for i in range(len(temperatures)):
            while (stack and temperatures[i] > stack[-1][0]):
                stackVal, stackInd = stack.pop()
                res[stackInd] = i - stackInd
            stack.append([temperatures[i], i])
        return res
