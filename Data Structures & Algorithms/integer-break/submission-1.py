class Solution:
    def integerBreak(self, n: int) -> int:
        memo = {}
        def dfs(num):
            if num in memo:
                return memo[num]
            if num == 1:
                return num

            maxProd = 1
            for i in range(1, num):
                factor = i
                factor2 = num - i
                maxProd = max(factor * factor2, factor * dfs(factor2), maxProd)
            
            memo[num] = maxProd
            return maxProd

        return dfs(n)