from typing import List
from collections import deque


class Solution:
    def bfs(self, x: int, y: int) -> List:
        nodes, queue = [], deque([(x, y)])
        while len(queue) > 0:
            print(queue)
            n = len(queue)
            for i in range(n):
                p, q = queue.popleft()
                nodes.append((p, q))
                for t in range(p + 1, q + 1):
                    queue.append((t, q))
        return nodes


if __name__ == '__main__':
    print(Solution().bfs(0, 3))

