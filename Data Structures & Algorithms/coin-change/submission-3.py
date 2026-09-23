class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        memoization = {}
        def recurse(cur):
            if cur in memoization:
                return memoization[cur]
            if cur == amount:
                return 0
            if cur  > amount:
                return 100001
    
            #return min of the for loop
            res = []
            for i in coins:
                res.append(recurse(cur + i))
            memoization[cur] = 1 + min(res)
            return memoization[cur]
        res = recurse(0)
        if res > 10000:
            return -1
        return res

        
            
            
        