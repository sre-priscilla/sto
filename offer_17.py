from typing import List


class Solution:
    def printNumbers(self, n: int) -> List[int]:
        return [x for x in range(1, 10**n)]


if __name__ == '__main__':
    print(Solution().printNumbers(1))
    print(Solution().printNumbers(2))

