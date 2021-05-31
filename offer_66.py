from typing import List


class Solution:
    # def constructArr(self, a: List[int]) -> List[int]:
    #     from copy import copy
        
    #     if len(a) <= 1:
    #         return a 
        
    #     n = len(a)
    #     dpL = copy(a)
    #     dpR = copy(a)
        
    #     p, q = 1, n - 2
    #     while p < n:
    #         dpL[p] = a[p] * dpL[p - 1]
    #         dpR[q] = a[q] * dpR[q + 1]
    #         p, q = p + 1, q - 1
        
    #     print(dpL, dpR)
        
    #     result = copy(a)
    #     result[0] = dpR[1]
    #     result[n - 1] = dpL[n - 2]
    #     for i in range(1, n - 1):
    #         result[i] = dpL[i - 1] * dpR[i + 1]
    #     return result

    def constructArr(self, a: List[int]) -> List[int]:
        result = [1] * len(a)
        for i in range(1, len(a)):
            result[i] = result[i - 1] * a[i - 1]
        tmp = 1
        for i in range(len(a) - 2, -1, -1): 
            tmp *= a[i + 1]
            result[i] *= tmp
        return result


result = Solution().constructArr([1, 2, 3, 4, 5])
print(result)
    
