class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        r = len(matrix) * len(matrix[0]) - 1

        while (l <= r):
            mid = (l + r) // 2
            n_ind = mid % len(matrix[0])
            m_ind = mid // len(matrix[0])

            if (matrix[m_ind][n_ind] > target):
                r = mid - 1
            elif (matrix[m_ind][n_ind] < target):
                l = mid + 1
            else:
                return True

        return False