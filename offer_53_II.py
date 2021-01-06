from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # i, j = 0, len(nums) - 1
        # while i <= j:
        #     m = i + (j - i) // 2
        #     if nums[m] == m:
        #         i = m + 1
        #     else:
        #         j = m - 1
        # return i

        i, j = 0, len(nums) - 1
        while i < j:
            m = i + (j - i) // 2
            if nums[m] == m:
                i = m + 1
            else:
                j = m
        return i + 1 if i == len(nums) - 1 and nums[i] == i else i

