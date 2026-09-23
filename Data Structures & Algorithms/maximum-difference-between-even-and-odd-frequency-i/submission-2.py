class Solution:
    def maxDifference(self, s: str) -> int:
        freq = {}

        for i in range(len(s)):
            freq[s[i]] = freq.get(s[i], 0) + 1

        min_even = float('inf')
        max_odd = 0
        for val in freq.values():
            if val % 2 == 0:
                min_even = min(val, min_even)
            else:
                max_odd = max(val, max_odd)

        return max_odd - min_even