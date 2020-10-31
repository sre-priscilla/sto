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

        # if len(prices) <= 1:
        #     return 0
        # dp = [price for price in prices]
        # for i in range(1, len(prices)):
        #     dp[i] = dp[i - 1] if prices[i] > dp[i - 1] else prices[i]
        # max_profit = 0
        # for i in range(1, len(prices)):
        #     max_profit = max(max_profit, prices[i] - dp[i])
        # return max_profit


        # if len(prices) <= 1:
        #     return 0
        # dp = [price for price in prices]
        # for i in range(len(prices) - 2, -1, -1):
        #     dp[i] = dp[i + 1] if prices[i] < dp[i + 1] else prices[i]
        # max_profit = 0
        # for i in range(len(prices) - 2, -1, -1):
        #     max_profit = max(max_profit, dp[i + 1] - prices[i])
        # return max_profit


