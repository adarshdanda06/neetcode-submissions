class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        gInd = 0
        sInd = 0

        g.sort()
        s.sort()

        while gInd < len(g) and sInd < len(s):
            if s[sInd] >= g[gInd]:
                gInd += 1
            sInd += 1

        return gInd

