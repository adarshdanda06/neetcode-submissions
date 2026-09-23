class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        arrMap = {}
        for i in range(len(position)):
            arrMap[position[i]] = speed[i]
        position.sort(reverse=True)

        prevTime = 0
        count = 0
        for i in position:
            time = (target - i)/arrMap[i]
            if (time > prevTime):
                count += 1
                prevTime = time
        return count