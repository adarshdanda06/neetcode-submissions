class Solution:
    def reorganizeString(self, s: str) -> str:
        countMap = {}
        for letter in s:
            countMap[letter] = countMap.get(letter, 0) + 1
        
        heap = []
        for letter, freq in countMap.items():
            heapq.heappush(heap, (-freq, letter))

        res = ""
        temp = None
        while heap:
            freq, letter = heapq.heappop(heap)
            if (not res) or (res and res[-1] != letter):
                res += letter
                freq += 1
                if freq != 0:
                    heapq.heappush(heap, (freq, letter))

            else:
                if not heap:
                    return ""
                temp = (freq, letter)
                newFreq, newLetter = heapq.heappop(heap)
                res += newLetter
                newFreq += 1
                if newFreq != 0:
                    heapq.heappush(heap, (newFreq, newLetter))
                heapq.heappush(heap, temp)
        
        return res
