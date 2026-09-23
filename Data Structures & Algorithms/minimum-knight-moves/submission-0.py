class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        q = deque([(0, 0)])
        
        count = 0
        visited = set()
        directions = [(-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1)]
        while q:
            currLen = len(q)
            for posInd in range(currLen):
                currX, currY = q.popleft()

                if currX == x and currY == y:
                    return count

                for d in directions:
                    newX = currX + d[1]
                    newY = currY + d[0]
                    newCoords = (newY, newX)
                    if newCoords not in visited:
                        q.append(newCoords)
                        visited.add(newCoords)


            count += 1

            
        return -1

