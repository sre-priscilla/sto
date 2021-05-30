 class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0:
            return 0
        result = 1
        if n < 0:
            x, n = 1 / x, -n
        while n:
            if n & 1:
                result *= x
            x *= x
            n >>= 1
        return result
