class Solution:
    def numDecodings(self, s: str) -> int:
        memoization = {}
        def recurse(i):

            if i == len(s):
                return 1
            
            if s[i] == '0':
                return 0
            

            if i < len(s) - 1 and int(s[i: i + 2]) <= 26:
                if i not in memoization:
                    memoization[i] = recurse(i + 1) + recurse(i + 2)
                return memoization[i]

            
            if i not in memoization:
                memoization[i] = recurse(i + 1)
            return memoization[i]
        
        return recurse(0)
        
        
    