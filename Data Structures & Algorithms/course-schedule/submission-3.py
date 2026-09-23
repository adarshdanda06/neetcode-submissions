class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if len(prerequisites) == 0:
            return True

        prereq_map = {}
        for pre in prerequisites:
            course = pre[0]
            prereq = pre[1]
            if course not in prereq_map:
                prereq_map[course] = set()

            if prereq not in prereq_map:
                prereq_map[prereq] = set()

            prereq_map[course].add(prereq)

        for num in range(numCourses):
            if num not in prereq_map:
                prereq_map[num] = set()

        added = set()
        visited = set()
        do_not_include = set()

        def dfs(key):
            vals_set = prereq_map[key]
            if len(vals_set) == 0:
                added.add(key)
                return
            
            for val in vals_set:
                if (val in visited):
                    do_not_include.update(visited)
                    continue

                visited.add(val)
                dfs(val)
                visited.remove(val)


            if val not in do_not_include:
                added.add(key)
            
        
        for key in prereq_map.keys():
            visited.add(key)
            dfs(key)
            visited.remove(key)

        return len(added) == numCourses