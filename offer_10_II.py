class Solution:
    def numWays(self, n: int) -> int:
        f0, f1 = 1, 1
        for _ in range(n):
            f0, f1 = f1, f0 + f1
        return f0 % 1000000007


if __name__ == '__main__':
    assert Solution().numWays(0) == 1
    assert Solution().numWays(2) == 2
    assert Solution().numWays(7) == 21