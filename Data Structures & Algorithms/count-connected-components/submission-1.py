class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        node_map = { i:set() for i in range(n) }

        for edge in edges:
            first = edge[0]
            second = edge[1]
            node_map[first].add(second)
            node_map[second].add(first)

        visited = set()

        def bfs(i):
            if i in visited:
                return

            q = deque([i])
            while q:
                node = q.popleft()
                visited.add(node)

                for nbor in node_map[node]:
                    if nbor in visited:
                        continue
                    q.append(nbor)

        count = 0
        for i in range(n):
            if i not in visited:
                count += 1
                bfs(i)

        return count
