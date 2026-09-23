class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        curr = ""
        res = []
        def dfs(opening, closing):
            nonlocal curr
            if opening > n or closing > n:
                return

            if opening == n and closing == n:
                res.append(curr)
                return

            if closing < opening:
                curr += ")"
                dfs(opening, closing + 1)
                curr = curr[:-1]

            curr += "("
            dfs(opening + 1, closing)
            curr = curr[:-1]
        dfs(0, 0)
        return res
        