class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memoization = {}
        def recurse_cost(i, tot):

            if (i >= len(cost)):
                return tot
            
            if (i + 1, tot + cost[i]) not in memoization:
                memoization[(i + 1, tot + cost[i])] = recurse_cost(i + 1, tot + cost[i])
            if (i + 2, tot + cost[i]) not in memoization:
                memoization[(i + 2, tot + cost[i])] = recurse_cost(i + 2, tot + cost[i])
            
            return min(memoization[(i + 1, tot + cost[i])], memoization[(i + 2, tot + cost[i])])
    

        
        return min(recurse_cost(0, 0), recurse_cost(1, 0))

        #2
        #1 2 3
        #1 3


        #2, 1, 2, 1, 1, 1
        #2, 1, 
        