class Solution:
    def fib(self, n: int) -> int:
        # if n <= 1:
        #     return n
        # return self.fib(n - 1) + self.fib(n - 2)

        if n <= 1:
            return n
        f0, f1 = 0, 1
        for i in range(n - 1):
            f0, f1 = f1, f0 + f1
        return f1 % (10**9 + 7)



if __name__ == '__main__':
    for i in range(10):
        print(Solution().fib(i))