class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        inDegree = {} # (r, c) -> indegreeCount

        # num of neighbors that is less than currNode val
            
        def inbounds(row, col):
            if row < 0 or row >= len(matrix) or col < 0 or col >= len(matrix[0]):
                return False
            
            return True

        def nodeGreaterThanNeighb(row, col, neighbRow, neigbhCol):
            if not inbounds(neighbRow, neigbhCol):
                return False

            return matrix[row][col] > matrix[neighbRow][neigbhCol]

        def nodeLessThanNeighb(row, col, neighbRow, neigbhCol):
            if not inbounds(neighbRow, neigbhCol):
                return False

            return matrix[row][col] < matrix[neighbRow][neigbhCol]
            
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                dirs = [(0, 1), (0, -1), (-1, 0), (1, 0)]
                inDegree[(row, col)] = 0
                for rDelta, cDelta in dirs:
                    if nodeGreaterThanNeighb(row, col, row+rDelta, col+cDelta):
                        inDegree[(row, col)] += 1

        q = deque()
        for key, val in inDegree.items():
            if val == 0:
                q.append(key)
        pathLen = 0

        while q:
            qLen = len(q)
            for i in range(qLen):
                currRow, currCol = q.popleft()
                dirs = [(0, 1), (0, -1), (-1, 0), (1, 0)]
                for rDelta, cDelta in dirs:
                    newRow = currRow + rDelta
                    newCol = currCol + cDelta
                    if nodeLessThanNeighb(currRow, currCol, newRow, newCol):
                        inDegree[(newRow, newCol)] -= 1
                        if inDegree[(newRow, newCol)] == 0:
                            q.append((newRow, newCol))


            pathLen += 1
        return pathLen
