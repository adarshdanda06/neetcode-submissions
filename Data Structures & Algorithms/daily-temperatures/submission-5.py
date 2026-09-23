class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        posStack = []
        for i in range(len(temperatures)):                
            while (len(posStack) > 0 and temperatures[i] > posStack[-1][0]):
                res[posStack[-1][1]] = i - posStack[-1][1]
                posStack.pop()
            posStack.append([temperatures[i], i])

        return res
                