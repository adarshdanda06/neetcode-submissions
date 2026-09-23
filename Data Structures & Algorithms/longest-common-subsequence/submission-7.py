class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text2)
        n = len(text1)
        # column represents text1
        # row represents text2

        cache = [[0 for _ in range(n + 1)] for _ in range(2)]

        for r in range(m - 1, -1, -1):
            for c in range(n - 1, -1, -1):
                if text1[c] == text2[r]:
                    cache[0][c] = 1 + cache[1][c + 1]
                else:
                    cache[0][c] = max(cache[0][c + 1], cache[1][c])

            cache[1] = cache[0][:]
        return cache[0][0]