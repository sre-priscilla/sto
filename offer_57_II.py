from typing import List
from math import sqrt

class Solution:
    def findContinuousSequence(self, target: int) -> List[List[int]]:
        # limit, ret = target // 2, []
        # for i in range(1, limit + 1):
        #     if target - i <= i:
        #         break
        #     _sum = 0
        #     for j in range(i, target):
        #         _sum += j
        #         if _sum > target:
        #             break
        #         elif _sum == target:
        #             ret.append([k for k in range(i, j + 1)])
        #             break
        # return ret

        # limit, ret = target // 2, []
        # for x in range(1, limit + 1):
        #     if target - x <= x:
        #         break
        #     delta = 1 - 4 * (x - x*x - 2 * target)
        #     if delta < 0:
        #         continue
        #     sqrt_delta = int(sqrt(delta + 0.5))
        #     if sqrt_delta * sqrt_delta == delta and (sqrt_delta - 1) % 2 == 0:
        #         y = int((sqrt_delta - 1) / 2)
        #         if y > x:
        #             ret.append([t for t in range(x, y + 1)])
        # return ret

        ret = []
        i, j, _sum = 1, 1, 0
        while i <= target // 2:
            if _sum < target:
                _sum, j = _sum + j, j + 1
            elif _sum > target:
                _sum, i = _sum - i, i + 1
            else:
                ret.append([k for k in range(i, j)])
                _sum, i = _sum - i, i + 1
        return ret




if __name__ == '__main__':
    print(Solution().findContinuousSequence(9))
