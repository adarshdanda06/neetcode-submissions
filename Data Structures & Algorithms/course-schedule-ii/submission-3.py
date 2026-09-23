class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adjList = { i:set() for i in range(numCourses) }
        for crs, pre in prerequisites:
            adjList[pre].add(crs)

        cycle = False
        reached = set()
        visited = set()
        dq = deque()

        def dfs(i):
            nonlocal cycle
            if i in reached:
                return

            reached.add(i)
            if cycle:
                return

            if len(adjList[i]) == 0:
                dq.appendleft(i)
                return
            
            visited.add(i)
            for crs in adjList[i]:
                if crs in visited:
                    cycle = True
                    return
                dfs(crs)

            dq.appendleft(i)
            visited.remove(i)

        for i in range(numCourses):
            dfs(i)
        
        return [] if cycle else list(dq)
            


        # reach cycle, check elem in vist set, if is, then cycle
        # bool flag

        # 0 -> 1 -> 3
        #   -> 2 ->


        # 


        # 0
        # 1 
        # 2


        # 0 1 2 -> creating a dif