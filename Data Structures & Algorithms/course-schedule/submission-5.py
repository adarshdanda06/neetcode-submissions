class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # dfs on ever course
        # build adj list

        adjList = { i:set() for i in range(numCourses) } # course to prereq mapping, check for 
        for crs, prereq in prerequisites:
            adjList[crs].add(prereq)

        # 1 -> 2 -> 0
        # 0: 2
        # 1: 
        # 2: 1

        visited = set()
        def dfs(i):
            if len(adjList[i]) == 0:
                return True
            if i in visited:
                return False

            visited.add(i)
            for crs in adjList[i]:
                if not dfs(crs):
                    return False

            visited.remove(i)
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False

        return True

        # prev = -1