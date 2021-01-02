from typing import List

class Solution:
    def minArray(self, numbers: List[int]) -> int:
        # for i in range(1, len(numbers)):
        #     if numbers[i] < numbers[0]:
        #         return numbers[i]
        # return numbers[0]

        l, h = 0, len(numbers) - 1
        while l < h:
            m = l + (h - l) // 2
            if numbers[m] < numbers[h]:
                h = m
            elif numbers[m] > numbers[h]:
                l = m + 1
            else:
                h -= 1
        return numbers[l]


if __name__ == '__main__':
    assert Solution().minArray([3,4,5,1,2]) == 1
    assert Solution().minArray([2,2,2,0,1]) == 0

