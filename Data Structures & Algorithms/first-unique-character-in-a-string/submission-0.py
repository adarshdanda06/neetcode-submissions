class Solution:
    def firstUniqChar(self, s: str) -> int:
        count_map = {}

        for i in range(len(s)):
            if s[i] in count_map:
                count_map[s[i]] += 1            
            else:
                count_map[s[i]] = 1


        for i in range(len(s)):
            if count_map[s[i]] == 1:
                return i

        return -1