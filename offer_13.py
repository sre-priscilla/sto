class Solution:
    def movingCount(self, m: int, n: int, k: int) -> int:
        def sum_digit(x):
            _sum = 0
            while x != 0:
                _sum += x % 10
                x //= 10
            return _sum
        
        from collections import deque
        
        result = 0
        queue, bitmap = deque([(0, 0)]), [0 for _ in range(m * n)]
        while queue:
            i, j = queue.popleft()
            if bitmap[i * n + j] != 1 and sum_digit(i) + sum_digit(j) <= k:
                bitmap[i * n + j] = 1
                result += 1
                if 0 <= i + 1 < m and 0 <= j < n:
                    queue.append((i + 1, j))
                if 0 <= i < m and 0 <= j + 1 < n:
                    queue.append((i, j + 1))
        return result
                
