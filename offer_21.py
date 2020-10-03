from typing import List

class Solution:
    def exchange(self, nums: List[int]) -> List[int]:
        i, n = 0, len(nums)
        for j in range(n):
            if nums[j] % 2 != 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
        return nums

