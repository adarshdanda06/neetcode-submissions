class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        pre_map = { i:set() for i in range(n) }
        
        for i in range(len(edges)):
            first = edges[i][0]
            second = edges[i][1]
            pre_map[first].add(second)
            pre_map[second].add(first)

        q = deque()
        visited = set([0])
        q.append((0, -1))

        while q:
            curr, parent = q.popleft()
            visited.add(curr)

            for node in pre_map[curr]:
                if node == parent:
                    continue

                if node in visited:
                    return False

                if node not in visited:
                    q.append((node, curr))

        
        return len(visited) == n


