class Solution:
    def numDecodings(self, s: str) -> int:

        # 1223 -> (1, 2, 2, 3), (12, 2, 3), (12, 23), (1, 2, 23) (1, 22, 3)
                                # i = 0 

                # i = 1  (1)                         # i = 2 (12, )

  #        (1, 2)        (1, 22)                 (12, 2, 3).  (12, 23)
        # i = 2      # i = 3                   # i = 3       # i = 4

#(1,x 2, 2).  (1, 2, 23). (1, 22, 3)
# i = 3      i = 4.       # i = 4
        # r
        memo = {}
        def dfs(i):
            if i in memo:
                return memo[i]
            if i >= len(s):
                return 1
            if s[i] == '0': # cant be on s[i] = 0
                return 0

            take1 = dfs(i + 1)
            take2Num = int(s[i:i+2])
            take2 = 0
            if i <= len(s) - 2 and take2Num >= 10 and take2Num <= 26:
                take2 = dfs(i + 2)
            res = take1 + take2
            memo[i] = res
            return res

        return dfs(0)



            


