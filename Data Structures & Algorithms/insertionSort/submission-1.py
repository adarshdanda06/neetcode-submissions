# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        i = 1
        out = []
        if (len(pairs) == 0):
            return out
        out.append(pairs[:])

        while(i < len(pairs)):
            j = i
            while(j > 0 and pairs[j].key < pairs[j-1].key):
                temp = pairs[j-1]
                pairs[j-1] = pairs[j]
                pairs[j] = temp
                j -= 1
            out.append(pairs[:])
            i += 1

        return out
