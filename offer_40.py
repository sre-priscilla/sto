from typing import List


def heapify(nums: List[int]):
    for i in reversed(range(len(nums) // 2)):
        print("sift_down", i)
        _shift_down(nums, i)


def heappop(nums: List[int]) -> int:
    nums[0], nums[-1] = nums[-1], nums[0]
    top = nums.pop()
    if len(nums) > 0:
        _shift_down(nums, 0)
    return top


def _shift_up(heap: List[int], i: int):
    while i > 0 and heap[i] < heap[(i - 1) // 2]:
        parent = (i - 1) // 2
        heap[i], heap[parent] = heap[parent], heap[i]
        i = parent


def _shift_down(heap: List[int], i: int):
    while i < len(heap) // 2:
        left, right = 2 * i + 1, 2 * i + 2
        _min = i
        if left < len(heap) and heap[_min] > heap[left]:
            _min = left
        if right < len(heap) and heap[_min] > heap[right]:
            _min = right
        if i == _min:
            break
        heap[i], heap[_min] = heap[_min], heap[i]
        i = _min

class Solution:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        # from heapq import heapify, heappop

        heapify(arr)
        ret = []
        for _ in range(k):
            ret.append(heappop(arr))
        return ret


if __name__ == '__main__':
    print(Solution().getLeastNumbers([3, 1, 2], 2))
    # nums = [7, 5, 19, 8, 4, 1, 20, 13, 14]
    # heapify(nums)
    # for _ in range(len(nums)):
    #     print(heappop(nums))