class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res, part = [], []

        def dfs(i):
            if i >= len(s):
                res.append(part.copy())
                return

            for j in range(i, len(s)):
                word = s[i:j+1]
                if (isPal(word)):
                    part.append(word)
                    dfs(j + 1)
                    part.pop()


        def isPal(word):
            if len(word) == 0:
                return False
            for i in range(len(word)):
                if word[i] != word[len(word) - 1 - i]:
                    return False
            return True

        dfs(0)
        return res
                
