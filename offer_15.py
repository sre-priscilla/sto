class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n != 0:
            count += n & 1
            n >>= 1
        return count


if __name__ == '__main__':
    assert Solution().hammingWeight(11) == 3
    assert Solution().hammingWeight(128) == 1
    assert Solution().hammingWeight(22685491128062564230891640495451214081) == 31