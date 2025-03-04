# 643.py
from functools import reduce

from test.test_suite import run_tests


class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        curr_sum = sum(nums[:k])
        max_sum = curr_sum
        for i in range(k, len(nums)):
            curr_sum = curr_sum - nums[i - k] + nums[i]
            max_sum = max(max_sum, curr_sum)
        return max_sum / k


test_cases = [
    {
        "method": "findMaxAverage",
        "nums": [1, 12, -5, -6, 50, 3],
        "k": 4,
        "expected": 12.75000,
        "case_id": 1
    },
    {
        "method": "findMaxAverage",
        "nums": [5],
        "k": 1,
        "expected": 5.00000,
        "case_id": 2
    },
    {
        "method": "findMaxAverage",
        "nums": [-1],
        "k": 1,
        "expected": -1.00000,
        "case_id": 3
    },
    {
        "method": "findMaxAverage",
        "nums": [-10000, -10000, -10000, -10000, -10000],
        "k": 5,
        "expected": -10000.00000,
        "case_id": 4
    },
    {
        "method": "findMaxAverage",
        "nums": [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        "k": 10,
        "expected": 1.00000,
        "case_id": 5
    },
    {
        "method": "findMaxAverage",
        "nums": [0, -1, 0, -2, 0, 3, 0, -4],
        "k": 3,
        "expected": 1.00000,
        "case_id": 6
    },
    {
        "method": "findMaxAverage",
        "nums": [-5, 0, 5, 0, -5],
        "k": 2,
        "expected": 2.50000,
        "case_id": 7
    },
    {
        "method": "findMaxAverage",
        "nums": [3, -1, 0, 2, -2, 0, 1, -3],
        "k": 4,
        "expected": 1.00000,
        "case_id": 8
    }
]

run_tests()
