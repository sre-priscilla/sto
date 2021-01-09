class Solution:
    def add(self, a: int, b: int) -> int:
        t = 0xffffffff
        a, b = a & t, b & t
        while b != 0:
            a, b = a ^ b, (a & b) << 1 & t
        return a if a <= 0x7fffffff else ~(a ^ t)
