class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        letters = {}
        for i in range(26):
            letters[chr(i + 65)] = 0

        l = 0
        maxLen = 0
        for r in range(len(s)):
            letters[s[r]] += 1
            while (r - l - max(letters.values()) + 1 > k):
                letters[s[l]] -= 1
                l += 1
            maxLen = max(r - l + 1, maxLen)
        
        return maxLen