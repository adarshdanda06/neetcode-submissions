class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        pre_map = { i:set() for i in range(numCourses) }
        n = numCourses
        in_degree = [0] * n
        for crs, pre in prerequisites:
            in_degree[crs] += 1
            pre_map[pre].add(crs)

        q = deque()
        for i in range(n):
            if in_degree[i] == 0:
                q.append(i)

        ind = 0
        top_order = [0] * n
        while q:
            crs = q.popleft()
            top_order[ind] = crs
            for next_crs in pre_map[crs]:
                in_degree[next_crs] -= 1
                if in_degree[next_crs] == 0:
                    q.append(next_crs)

            ind += 1

        if ind != n:
            return []
        return top_order
