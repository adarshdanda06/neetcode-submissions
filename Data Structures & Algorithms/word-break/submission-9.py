class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memoization = {}
        def recurse(string):
            if string in memoization:
                return memoization[string]
            if len(string) == 0:
                return True
            for i in range(len(wordDict)):
                word = wordDict[i]
                if string[:len(word)] == word:
                    if recurse(string[len(word):]):
                        memoization[string] = True
                        return True
            memoization[string] = False
            return False
        return recurse(s)
                    #currently don't understand syntax for this: recurse old string in next word
        #removing words from string
        #obs: not all words need to be used & can reuse words
        #when done sequentially, not necessary removed
        #try to remove a word, put it back and try to remove next word