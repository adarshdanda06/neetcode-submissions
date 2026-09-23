class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        #for a subsequence, you either add or don't add el[i]
        #any subseq from a == any subseq from b

        #first generate all the subseq of a
        #generate all the subseq of b
        #find longest ones that match

        memoization = [[-1 for _ in range(len(text2))] for _ in range(len(text1))]
        def recurse(i, j):
            if i >= len(text1) or j >= len(text2):
                return 0
            if memoization[i][j] != -1:
                return memoization[i][j]
            
            if text1[i] == text2[j]:
                memoization[i][j] = 1 + recurse(i + 1, j + 1)
                return memoization[i][j]
            
            memoization[i][j] = max(recurse(i + 1, j), recurse(i, j + 1))
            return memoization[i][j]
        return recurse(0, 0)   

        