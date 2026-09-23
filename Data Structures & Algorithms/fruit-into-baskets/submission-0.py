class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        # map of count of fruits we in basket
        # fruit Type is key
        # count is value

        # l, r = 0, 0
        # iter r to end
            # 

        fruitCount = {}
        l = 0
        maxCount = 0

        for r in range(len(fruits)):
            fruitType = fruits[r]
            fruitCount[fruitType] = fruitCount.get(fruitType, 0) + 1

            while len(fruitCount.keys()) > 2:
                lFruitType = fruits[l]
                fruitCount[lFruitType] = fruitCount[lFruitType] - 1
                if fruitCount[lFruitType] == 0:
                    fruitCount.pop(lFruitType, None)
                l += 1
            
            currSum = 0
            for value in fruitCount.values():
                currSum += value
            maxCount = max(currSum, maxCount)

        return maxCount
            