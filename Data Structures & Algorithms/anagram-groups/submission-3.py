class Solution:
    from collections import defaultdict
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #group all anagrams together
        #all words that have the same character count from a-z should be grouped together
        #also know all lowercase so don't need to change anything
        ans = []
        hash_map = {}
        for word in strs:
            cur_hash = defaultdict(int)
            for c in word:
                cur_hash[c] += 1
            hashable_key = tuple(sorted(cur_hash.items()))
            if hashable_key in hash_map:
                hash_map[hashable_key].append(word)
            else:
                hash_map[hashable_key] = [word]
        
        for i in hash_map:
            ans.append(hash_map[i])
        return ans

