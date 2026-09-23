import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        ans = []
        for i in range(len(points)):
            dist = points[i][0] * points[i][0]  + points[i][1] * points[i][1]
            dist = dist ** 0.5
            heapq.heappush(heap, (dist, i))
        
        for i in range(k):
            dist, ind = heapq.heappop(heap)
            ans.append(points[ind])
        return ans