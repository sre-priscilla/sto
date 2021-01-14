from typing import List


class Solution:
    # def isStraight(self, nums: List[int]) -> bool:
    #     rs = set()
    #     _min, _max = 14, 0
    #     for num in nums:
    #         if num == 0:
    #             continue
    #         _min = min(_min, num)
    #         _max = max(_max, num)
    #         if num in rs:
    #             return False
    #         rs.add(num)
    #     return _max - _min < 5

    def isStraight(self, nums: List[int]) -> bool:
        nums.sort()
        joker = 0
        for i in range(4):
            if nums[i] == 0:
                joker += 1
            elif nums[i] == nums[i+1]:
                return False
        return nums[4] - nums[joker] < 5




if __name__ == '__main__':
    print(Solution().isStraight([1, 2, 3, 4, 5]))