class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        new_points = []

        for i in range(len(points)):
            dist = (((points[i][0])**2 + (points[i][1])**2) ** (0.5), (points[i][0], points[i][1]))
            heapq.heappush(new_points, dist)

        ans = []
        for i in range(k):
            val = heapq.heappop(new_points)
            ans.append(val[1])

        return ans