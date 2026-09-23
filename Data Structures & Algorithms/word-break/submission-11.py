class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memoization = {}
        def recurse(i):
            if i in memoization:
                return memoization[i]
            if i >= len(s):
                return True
            
            for word in wordDict:
                if s[i: i + len(word)] == word:
                    if (recurse(i + len(word))):
                        memoization[i] = True
                        return True
            memoization[i] = False
            return False
        return recurse(0)