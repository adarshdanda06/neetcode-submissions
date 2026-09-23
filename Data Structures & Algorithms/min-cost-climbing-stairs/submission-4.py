class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memoization = {}
        #specific index: all future work will be repeated
        #memoization is related to specific index
        #lowest total from that index
        def recurse_cost(i):
    
            if (i >= len(cost)):
                return 0
            
            if i not in memoization:
                memoization[i] = cost[i] + min(recurse_cost(i + 1), recurse_cost(i + 2))
            
            return memoization[i]
        return min(recurse_cost(0), recurse_cost(1))

