class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        q = []

        for stone in stones:
            heapq.heappush(q, stone * -1)

        while len(q) > 1:
            val1 = -1 * heapq.heappop(q)
            val2 = -1 * heapq.heappop(q)

            if val1 != val2:
                diff = abs(val1 - val2)
                heapq.heappush(q, diff * -1)

        return 0 if len(q) == 0 else q[0] * -1
            