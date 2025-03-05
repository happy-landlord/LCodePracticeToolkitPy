# 33.py
from test.test_suite import run_tests


class Solution:
    def search(self, nums: list[int], target: int) -> int:
        pass


test_cases = [
    {
        "method": "search",
        "nums": [4, 5, 6, 7, 0, 1, 2],
        "target": 0,
        "expected": 4,
        "case_id": 1
    },
    {
        "method": "search",
        "nums": [4, 5, 6, 7, 0, 1, 2],
        "target": 3,
        "expected": -1,
        "case_id": 2
    },
    {
        "method": "search",
        "nums": [1],
        "target": 0,
        "expected": -1,
        "case_id": 3
    },
    {
        "method": "search",
        "nums": [1],
        "target": 1,
        "expected": 0,
        "case_id": 4
    },
    {
        "method": "search",
        "nums": [8, 9, 2, 3, 4],
        "target": 9,
        "expected": 1,
        "case_id": 5
    },
    {
        "method": "search",
        "nums": [5, 6, 7, 8, 9, 1, 2, 3, 4],
        "target": 6,
        "expected": 1,
        "case_id": 6
    }
]
run_tests()
