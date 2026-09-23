class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = set()

        def backtrack(cur_string, st_left, end_left):
            #st_left >= end_left at all times
            if (st_left == 0 and end_left == 0):
                ans.add(cur_string[:])
                return
            if (st_left < 0):
                return


            backtrack(cur_string + '(', st_left -1, end_left)
            if (st_left < end_left):
                backtrack(cur_string + ')', st_left, end_left - 1)
        
        backtrack('(', n - 1, n)
        return list(ans)


        

            








