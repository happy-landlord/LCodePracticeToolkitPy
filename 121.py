# 121.py
from test.test_suite import run_tests


# class Solution:
#     def maxProfit(self, prices: list[int]) -> int:
#         max_profit = 0
#         buy = 0
#
#         for sell in range(1, len(prices)):
#             # 如果找到更低的买入点，更新买入点
#             if prices[sell] < prices[buy]:
#                 buy = sell
#             # 否则计算当前利润并更新最大利润
#             else:
#                 current_profit = prices[sell] - prices[buy]
#                 max_profit = max(max_profit, current_profit)
#
#         return max_profit


class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        if not prices:
            return 0

        min_price = float('inf')
        max_profit = 0

        for price in prices:
            if price < min_price:
                min_price = price
            elif price - min_price > max_profit:
                max_profit = price - min_price

        return max_profit

test_cases = [
    {
        "method": "maxProfit",
        "prices": [7, 1, 5, 3, 6, 4],
        "expected": 5,
        "case_id": 1
    },
    {
        "method": "maxProfit",
        "prices": [7, 6, 4, 3, 1],
        "expected": 0,
        "case_id": 2
    },
    {
        "method": "maxProfit",
        "prices": [2, 4, 1],
        "expected": 2,
        "case_id": 3
    },
    {
        "method": "maxProfit",
        "prices": [3, 3, 3, 3, 3],
        "expected": 0,
        "case_id": 4
    },
    {
        "method": "maxProfit",
        "prices": [1, 2, 3, 4, 5],
        "expected": 4,
        "case_id": 5
    },
    {
        "method": "maxProfit",
        "prices": [9, 1, 10],
        "expected": 9,
        "case_id": 6
    }
]

run_tests()
