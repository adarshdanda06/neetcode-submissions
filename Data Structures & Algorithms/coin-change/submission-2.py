class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        memoization = {}
        def recurse(cur):
            if cur == amount:
                return 0
            if cur  > amount:
                return 100001
            #return min of the for loop
            res = []
            for i in coins:
                if cur + i not in memoization:
                    memoization[cur + i] = recurse(cur + i)
                res.append(memoization[cur + i])
            return 1 + min(res)

        res = recurse(0)
        if res > 10000:
            return -1
        return res

        
            
            
        