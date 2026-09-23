class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        table = {
                    2: 'abc',
                    3: 'def',
                    4: 'ghi',
                    5:'jkl',
                    6: 'mno',
                    7: 'pqrs',
                    8: 'tuv',
                    9: 'wxyz'
                }

        res, curr = [], ""
        def dfs(i):
            nonlocal curr
            if i >= len(digits):
                if len(curr) > 0:
                    res.append(curr)
                return

            num = int(digits[i])
            for letter in table[num]:
                curr += letter
                dfs(i + 1)
                curr = curr[:-1]

        dfs(0)
        return res