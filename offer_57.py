from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i, j = 0, len(nums) - 1
        while i < j:
            print(i, j)
            _sum = nums[i] + nums[j]
            if _sum > target:
                j -= 1
            elif _sum < target:
                i += 1
            else:
                return [nums[i], nums[j]]
        return []


if __name__ == '__main__':
    print(Solution().twoSum([2, 7, 11, 15], 9))
    print(Solution().twoSum([10, 26, 30, 31, 47, 60], 40))
    print(Solution().twoSum([1, 3, 5, 7, 8], 12))
