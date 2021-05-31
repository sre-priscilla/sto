from typing import List


class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        i, stack = 0, []
        for x in pushed:
            stack.append(x)
            while stack and stack[-1] == popped[i]:
                stack.pop()
                i += 1
        return len(stack) == 0


if __name__ == '__main__':
    print(Solution().validateStackSequences([1, 2, 3, 4, 5], [4, 5, 3, 2, 1]))
    print(Solution().validateStackSequences([1, 2, 3, 4, 5], [4, 3, 5, 1, 2]))
