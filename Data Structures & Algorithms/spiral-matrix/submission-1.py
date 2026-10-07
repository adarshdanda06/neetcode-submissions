class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        def inbounds(r, c):
            if r < 0 or c < 0 or r >= len(matrix) or c >= len(matrix[0]):
                return False
            return True
        
        nextDirs = {
            'right': 'down',
            'down': 'left',
            'left': 'up',
            'up': 'right'
        }
        moveInDirs = {
            'right': (0, 1),
            'down': (1, 0),
            'left': (0, -1),
            'up': (-1, 0)
        }

        pos = (0, 0)
        currDirection = 'right'
        visited = set()
        res = []

        while True:
            if len(res) == len(matrix) * len(matrix[0]):
                return res
            if pos in visited:
                return res
            visited.add(pos)
            r, c = pos
            res.append(matrix[r][c])
            nextPotentialPos = r + moveInDirs[currDirection][0], c + moveInDirs[currDirection][1]

            if inbounds(nextPotentialPos[0], nextPotentialPos[1]) and nextPotentialPos not in visited:
                pos = nextPotentialPos
            else:
                currDirection = nextDirs[currDirection]
                nextPotentialPos = r + moveInDirs[currDirection][0], c + moveInDirs[currDirection][1]
                pos = nextPotentialPos

        return []
        

