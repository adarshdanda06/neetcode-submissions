class Solution:
    from collections import defaultdict
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #group all anagrams together
        #all words that have the same character count from a-z should be grouped together
        #also know all lowercase so don't need to change anything
        ans = []
        hash_map = {}
        for word in strs:
            count = [0] * 26
            for c in word:
                count[ord(c) - ord('a')] += 1
            count = tuple(count)
            if count in hash_map:
                hash_map[count].append(word)
            else:
                hash_map[count] = [word]
        
        for i in hash_map:
            ans.append(hash_map[i])
        return ans

