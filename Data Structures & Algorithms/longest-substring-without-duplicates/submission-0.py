class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        str_map = {}

        l = 0
        max_len = 0
        for r in range(len(s)):
            str_map[s[r]] = str_map.get(s[r], 0) + 1
            while (str_map[s[r]] > 1):
                str_map[s[l]] -= 1
                l += 1
            
            max_len = max(r + 1 - l, max_len)

        return max_len