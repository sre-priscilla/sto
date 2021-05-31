class Solution:
    # solution 1
    # def __init__(self):
    #     self.res = 0
    
    # def sumNums(self, n: int) -> int:
    #     n > 1 and self.sumNums(n - 1)
    #     self.res += n
    #     return self.res

    # solution 2
    # def sumNums(self, n: int) -> int:
    #     res = 0

    #     def help(k: int):
    #         nonlocal res
    #         k > 1 and help(k - 1)
    #         res += k
        
    #     help(n)
    #     return res

    # solution 3
    def sumNums(self, n: int) -> int:
        res, a, b = 0, n, n + 1

        def add(x: int):
            nonlocal res
            res += x

        def shift():
            nonlocal res, a, b
            b & 1 and add(a)
            a <<= 1
            b >>= 1

        def help():
            shift()
            b != 0 and help()
        
        help()
        return res >> 1


print(Solution().sumNums(3))