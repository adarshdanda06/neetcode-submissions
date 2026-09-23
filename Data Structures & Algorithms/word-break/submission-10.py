class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memoization = {}
        def recurse(i):
            if i in memoization:
                return memoization[i]
            if i >= len(s):
                return True
            for j in range(len(wordDict)):
                word = wordDict[j]
                if s[i: i + len(word)] == word:
                    if recurse(i + len(word)):
                        memoization[i] = True
                        return True
            memoization[i] = False
            return False
        return recurse(0)
                    #currently don't understand syntax for this: recurse old string in next word
        #removing words from string
        #obs: not all words need to be used & can reuse words
        #when done sequentially, not necessary removed
        #try to remove a word, put it back and try to remove next word