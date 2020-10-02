import ipdb
from typing import List


class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        # n = len(nums)
        # for i in range(n):
        #     if i == nums[i]:
        #         continue
        #     while i != nums[i]:
        #         j = nums[i]
        #         if nums[i] == nums[j]:
        #             return nums[i]
        #         nums[i], nums[j] = nums[j], nums[i]
        # return -1

        i, n = 0, len(nums)
        while i < n:
            if nums[i] == i:
                i += 1
                continue
            j = nums[i]
            if nums[i] == nums[j]:
                return nums[i]
            nums[i], nums[j] = nums[j], nums[i]
        return -1



def test_solution():
    print(Solution().findRepeatNumber([2, 3, 1, 0, 2, 5, 3]))

    # nums = [2, 3, 1, 0, 2, 5, 3]
    # nums[0], nums[2] = nums[2], nums[0]
    # print(nums)