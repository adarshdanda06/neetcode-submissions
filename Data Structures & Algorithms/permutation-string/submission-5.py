class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1Dict = {}
        for letter in s1:
            s1Dict[letter] = s1Dict.get(letter, 0) + 1
        # asd
        # as
        s2Dict = {}
        l = 0
        for r in range(len(s2)):
            s2Dict[s2[r]] = s2Dict.get(s2[r], 0) + 1
            if (r - l >= len(s1)):
                s2Dict[s2[l]] = s2Dict.get(s2[l], 0) - 1
                if (s2Dict[s2[l]] == 0):
                    del s2Dict[s2[l]]
                l += 1
            if (s1Dict == s2Dict):
                return True
        return False
        

        # abc 
        # lecabee
        # create a dict out of s1 (letter to count)
        # iter thru the s2, if we have a count that exceeds dict letter count
        # then increase left pointer and subtract the old letters and keep going 
        # thru the str and until all counts are less than or equal to the counts
        # in original
        # if s1 dict == s2 dict that we get return true
        # if the loop reaches the end, the return false
        # r - l pointer needs to be less than s1 len