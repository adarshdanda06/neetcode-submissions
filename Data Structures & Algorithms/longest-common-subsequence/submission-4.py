class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text2)
        n = len(text1)
        # column represents text1
        # row represents text2

        cache = [[0 for _ in range(n + 1)] for __ in range(m + 1)]

        for r in range(m - 1, -1, -1):
            for c in range(n - 1, -1, -1):
                if text1[c] == text2[r]:
                    cache[r][c] = 1 + cache[r + 1][c + 1]
                else:
                    cache[r][c] = max(cache[r+1][c], cache[r][c+1])

        return cache[0][0]