class Solution:
    # def cuttingRope(self, n: int) -> int:
    #     import math

    #     if n <= 3:
    #         return n - 1
    #     a, b = n // 3, n % 3
    #     if b == 0:
    #         return int(math.pow(3, a))
    #     if b == 1:
    #         return int(math.pow(3, a - 1) * 4)
    #     return int(math.pow(3, a) * 2)

    def cuttingRope(self, n: int) -> int:
        if n <= 3:
            return n - 1
        result = 1
        while n > 4:
            n -= 3
            result *= 3
        return n * result