from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0
        ret, _min = 0, prices[0]
        for i in range(1, len(prices)):
            if prices[i] < _min:
                _min = prices[i]
            else:
                ret = max(ret, prices[i] - _min)
        return ret
