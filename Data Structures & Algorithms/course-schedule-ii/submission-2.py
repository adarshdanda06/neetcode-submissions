class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        pre_map = { i:[] for i in range(numCourses) }
        in_deg = [0] * numCourses

        for crs, pre in prerequisites:
            in_deg[crs] += 1
            pre_map[pre].append(crs)

        q = deque()
        for i in range(numCourses):
            if (in_deg[i] == 0):
                q.append(i)

        res = []
        while q:
            node = q.popleft()

            for val in pre_map[node]:
                in_deg[val] -= 1
                if in_deg[val] == 0:
                    q.append(val)

            res.append(node)

        return res if len(res) == numCourses else []