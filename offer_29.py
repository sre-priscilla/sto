from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ret = []
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return ret
        m, n = len(matrix), len(matrix[0])

        p, q = 0, 0
        while p < m and q < n:
            for j in range(p, n):
                ret.append(matrix[p][j])
            for i in range(p + 1, m - 1):
                ret.append(matrix[i][n - 1])
            if p != m - 1:
                for j in reversed(range(q, n)):
                    ret.append(matrix[m - 1][j])
            if q != n - 1:
                for i in reversed(range(p + 1, m - 1)):
                    ret.append(matrix[i][q])
            m, n = m - 1, n - 1
            p, q = p + 1, q + 1
        return ret




if __name__ == '__main__':
    print(Solution().spiralOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
