class Solution:
    def lastRemaining(self, n: int, m: int) -> int:
        # def f(_n: int, _m: int) -> int:
        #     if _n == 0:
        #         return 0
        #     x = f(_n - 1, _m)
        #     return (_m + x) % _n
        # return f(n, m)

        ret = 0
        for i in range(2, n + 1):
            ret = (ret + m) % i
        return ret


if __name__ == '__main__':
    print(Solution().lastRemaining(5, 3))
