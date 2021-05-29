from typing import List
from collections import deque


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        deltas = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        def dfs(i: int, j: int, k: int) -> bool:
            if board[i][j] != word[k]:
                return False
            if k == len(word) - 1:
                return True
            board[i][j] = ' '
            result = False
            for delta in deltas:
                di, dj = delta
                if (not result) and (0 <= i + di < m) and (0 <= j + dj < n):
                    result |= dfs(i + di, j + dj, k + 1)
            board[i][j] = word[k]
            return result


        for i in range(m):
            for j in range(n):
                if dfs(i, j, 0):
                    return True
        return False
        


if __name__ == '__main__':
    # board = [
    #     ['A', 'B', 'C', 'E'],
    #     ['S', 'F', 'C', 'S'],
    #     ['A', 'D', 'E', 'E']
    # ]
    # word = 'ABCCED'
    # print(Solution().exist(board, word))

    # board = [['a']]
    # word = 'ab'
    # print(Solution().exist(board, word))

    board = [
        ['A', 'B', 'C', 'E'],
        ['S', 'F', 'E', 'S'],
        ['A', 'D', 'E', 'E']
    ]
    word = 'ABCESEEEFS'
    # print(Solution().exist(board, word))
    print(Solution().bfs(0, 0, board, word))