class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        b = 0
        t = len(matrix) - 1
        m = 0
        while b <= t:
            m = (b + t) // 2
            if target in range(matrix[m][0], matrix[m][-1] + 1):
                break
            elif matrix[m][0] > target:
                t = m - 1
            else:
                b = m + 1
        r = m
        b = 0
        t = len(matrix[r]) - 1
        while b <= t:
            m = (b + t) // 2
            if matrix[r][m] == target:
                return True
            elif matrix[r][m] > target:
                t = m - 1
            else:
                b = m + 1
        return False
