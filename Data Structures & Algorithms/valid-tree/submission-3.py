from collections import defaultdict
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) > n - 1:
            return False
        #no cycles, no disconnected
        hash_map = defaultdict(set)
        for node1, node2 in edges:
            hash_map[node1].add(node2)
            hash_map[node2].add(node1)


        visited = set()
        def dfs(node, par):
            if node in visited:
                return False
            
            visited.add(node)
            for adj in hash_map[node]:
                if adj == par:
                    continue
                dfs(adj, node)
            return True
        
        if dfs(0, -1) and len(visited) == n:
            return True
        return False