class Solution:
    def numDecodings(self, s: str) -> int:
        count = 0

        def dfs(i):
            nonlocal count
            if i >= len(s):
                count += 1
                return
            
            if s[i] == '0':
                return

            if i + 1 < len(s) and (s[i] == '1' or (s[i] == '2' and s[i + 1] in '0123456')):
                dfs(i + 2)

            dfs(i + 1)

        dfs(0)
        return count
            


