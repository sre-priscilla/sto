from typing import List, Deque


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        from collections import deque

        # n = len(nums)
        # ret, queue = [], deque()
        # for i, j in zip(range(1 - k, n + 1 - k), range(n)):
        #     if i > 0 and queue[0] == nums[i - 1]:
        #         queue.popleft()
        #     while queue and queue[-1] < nums[j]:
        #         queue.pop()
        #     queue.append(nums[j])
        #     if i >= 0:
        #         ret.append(queue[0])
        # return ret

        n, ret = len(nums), []
        if len(nums) == 0 or k == 0:
            return ret
        queue = deque()
        for i in range(k):
            while queue and queue[-1] < nums[i]:
                queue.pop()
            queue.append(nums[i])
        ret.append(queue[0])
        for i in range(k, n):
            if queue[0] == nums[i - k]:
                queue.popleft()
            while queue and queue[-1] < nums[i]:
                queue.pop()
            queue.append(nums[i])
            ret.append(queue[0])
        return ret



if __name__ == '__main__':
    print(Solution().maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3))
