class Solution:
    def leadsToDestination(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        # The number of possible paths from source to destination is a finite number - means that anything with a loop is false

        # run cycle detection on the graph
            # if we have a cycle return false
        neighborMap = {}
        for edge in edges:
            src, dst = edge
            if src not in neighborMap:
                neighborMap[src] = []
            neighborMap[src].append(dst)

        visited = set()
        dp = {}

        def dfs(node):
            if node in dp:
                return dp[node]
            
            neighborList = neighborMap.get(node, [])
            if node == destination:
                if len(neighborList) > 0:
                    return False
                dp[node] = True
                return True

            if node in visited: # cycle detection here
                dp[node] = False
                return False

            visited.add(node)
            res = True

            if len(neighborList) == 0:
                return False

            for neighbor in neighborList:
                res = res and dfs(neighbor)

            visited.remove(node)
            
            dp[node] = res
            return res

        result = dfs(source)
        if not result:
            return False

        for i in range(n):
            if dp.get(i, False) == False:
                return False

        return True

