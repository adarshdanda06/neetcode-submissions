from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mySet = set()
        for s in strs:
            mySet.add(''.join(sorted(s)))
        
        myDict = defaultdict(list)
        for s in strs:
            myDict[''.join(sorted(s))].append(s)

        res = []
        for values in myDict.values():
            res.append(values)
        return res