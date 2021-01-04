from typing import List


class Solution:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        from heapq import heapify, heappop
        #
        # heapify(arr)
        # ret = []
        # for _ in range(k):
        #     ret.append(heappop(arr))
        # return ret

        def heapify(nums: List[int]):
            pass

        def heappop(nums: List[int]) -> int:
            pass

        heapify(arr)
        ret = []
        for _ in range(k):
            ret.append(heappop(arr))
        return ret


if __name__ == '__main__':
    print(Solution().getLeastNumbers([3, 1, 2], 2))