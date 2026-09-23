class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        prereqMap = {}
        for prereq, course in prerequisites:
            if course not in prereqMap:
                prereqMap[course] = set()
            prereqMap[course].add(prereq)
        
        memo = {}
        def dfs(source, target):
            if (source, target) in memo:
                return memo[(source, target)]
            if source == target:
                return True

            if source not in prereqMap:
                return False

            prereqs = prereqMap[source]
            hasTarget = False
            for prereq in prereqs:
                hasTarget = hasTarget or dfs(prereq, target)
            memo[(source, target)] = hasTarget
            return hasTarget

        res = []
        for target, course in queries:
            res.append(dfs(course, target))

        return res
            