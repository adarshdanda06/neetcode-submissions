class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        total = 0
        gInd = 0
        sInd = 0

        g.sort()
        s.sort()

        while gInd < len(g) and sInd < len(s):
            if s[sInd] >= g[gInd]:
                sInd += 1
                gInd += 1
                total += 1
            
            else:
                sInd += 1

        return gInd

