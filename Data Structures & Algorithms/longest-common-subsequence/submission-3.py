class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        cache = {}

        def dfs(f, s):
            if f >= len(text1) or s >= len(text2):
                return 0

            if (f, s) in cache:
                return cache[(f, s)]

            if text1[f] == text2[s]:
                cache[(f, s)] = 1 + dfs(f + 1, s + 1)
                return cache[(f, s)]
            else:
                cache[(f, s)] = max(dfs(f, s + 1),
                    dfs(f + 1, s))

                return cache[(f, s)]

        return dfs(0, 0)