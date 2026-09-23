class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cache = {}
        def recurse(i):
            if (i >= len(cost)):
                return 0

            cache[i] = cost[i] + min(recurse(i + 1), recurse(i + 2))
            return cache[i]
        
        return min(recurse(0), recurse(1))