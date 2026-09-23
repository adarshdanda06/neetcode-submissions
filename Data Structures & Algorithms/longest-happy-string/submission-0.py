class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        heap = []

        if a > 0:
            heapq.heappush(heap, (-a, "a"))
        if b > 0:
            heapq.heappush(heap, (-b, "b"))
        if c > 0:
            heapq.heappush(heap, (-c, "c"))

        builtS = ""
        while heap:
            freq, letter = heapq.heappop(heap)
            
            if letter * 2 == builtS[-2:]:
                if len(heap) == 0:
                    break

                newFreq, newLetter = heapq.heappop(heap)
                builtS += newLetter
                newFreq += 1
                if newFreq < 0:
                    heapq.heappush(heap, (newFreq, newLetter))
            
            freq += 1
            builtS += letter
            if freq < 0:
                heapq.heappush(heap, (freq, letter))

        return builtS