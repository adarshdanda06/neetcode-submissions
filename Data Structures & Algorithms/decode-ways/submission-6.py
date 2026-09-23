class Solution:
    def numDecodings(self, s: str) -> int:
        memoization = {}
        def recurse(i):
            if i == len(s):
                return 1
            
            if s[i] == '0':
                return 0
            
            if i < len(s) - 1 and int(s[i:i + 2]) < 27:
                return recurse(i + 1) + recurse(i + 2)
            
            return recurse(i + 1)
        return recurse(0)
        
        
    