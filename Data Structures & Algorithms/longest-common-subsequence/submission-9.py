class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:


# t rabt. at abt
    # if both eq -> inc both pointer  (add 1 to ans)
    # otherwise
        # choice 1: move 1st pointer 1
        # choice 2: move 2nd pointer 1

        memo = [[-1 for i in range(len(text2))] for j in range(len(text1))]
        def dfs(p1, p2):
            if p1 >= len(text1) or p2 >= len(text2):
                return 0

            if memo[p1][p2] != -1:
                return memo[p1][p2]

            if text1[p1] == text2[p2]:
                memo[p1][p2] = dfs(p1 + 1, p2 + 1) + 1
            else:
                memo[p1][p2] = max(dfs(p1, p2 + 1), dfs(p1 + 1, p2))
            return memo[p1][p2]
            

        return dfs(0, 0)
        