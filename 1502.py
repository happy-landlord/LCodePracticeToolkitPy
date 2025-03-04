# 1502.py
from test.test_suite import run_tests


class Solution:
    def canMakeArithmeticProgression(self, arr: list[int]) -> bool:
        n = len(arr)
        min_val, max_val = min(arr), max(arr)

        d, remainder = divmod(max_val - min_val, n - 1)
        if remainder != 0:  # 如果余数不是 0，说明无法形成等差数列
            return False

        seen = set(arr)  # O(n) 存储所有元素
        return all(min_val + i * d in seen for i in range(n))  # O(n)


test_cases = [
    {
        "method": "canMakeArithmeticProgression",
        "arr": [3, 5, 1],
        "expected": True,
        "case_id": 1
    },
    {
        "method": "canMakeArithmeticProgression",
        "arr": [1, 2, 4],
        "expected": False,
        "case_id": 2
    },
    {
        "method": "canMakeArithmeticProgression",
        "arr": [7, 3, 5, 1],
        "expected": True,
        "case_id": 3
    },
    {
        "method": "canMakeArithmeticProgression",
        "arr": [1, 3, 3, 7],
        "expected": False,
        "case_id": 4
    },
    {
        "method": "canMakeArithmeticProgression",
        "arr": [10, 0, 5, -5],
        "expected": True,
        "case_id": 5
    }
]
run_tests()
