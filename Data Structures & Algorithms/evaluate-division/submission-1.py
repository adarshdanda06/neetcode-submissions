class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        visited = set()
        foundTarget = False
        def dfs(startVar, targetVar):
            nonlocal foundTarget
            if startVar in visited:
                return -1.0

            varsDict = systemOfEqs[startVar]
            if targetVar in varsDict:
                foundTarget = True
                return varsDict[targetVar]

            visited.add(startVar)
            pathProduct = 0.0
            for var2, value in varsDict.items():
                pathProduct = max(dfs(var2, targetVar) * value, pathProduct)
            visited.remove(startVar)

            return pathProduct if foundTarget else -1.0

        systemOfEqs = defaultdict(dict)
        for i in range(len(equations)):
            equation = equations[i]
            value = values[i]
            var1, var2 = equation

            systemOfEqs[var1][var2] = value
            systemOfEqs[var2][var1] = 1.0 / value
        print(systemOfEqs)

        quotients = []
        for query in queries:
            var1, var2 = query
            if var1 not in systemOfEqs or var2 not in systemOfEqs:
                quotients.append(-1.0)
                continue

            if var1 == var2:
                quotients.append(1.0)
                continue
            foundTarget = False
            quotients.append(dfs(var1, var2))
            
        return quotients

        """



        # a / c = 4
        # b / a = 0.25
        # c / c = 1
        # ab / a = -1
        # d / d = -1
        """