# 15.py
from test.test_suite import run_tests


class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        pass


test_cases = [
    {
        "method": "threeSum",
        "nums": [-1, 0, 1, 2, -1, -4],
        "expected": [[-1, -1, 2], [-1, 0, 1]],
        "case_id": 1
    },
    {
        "method": "threeSum",
        "nums": [0, 1, 1],
        "expected": [],
        "case_id": 2
    },
    {
        "method": "threeSum",
        "nums": [0, 0, 0],
        "expected": [[0, 0, 0]],
        "case_id": 3
    },
    {
        "method": "threeSum",
        "nums": [-2, 0, 1, 1, 2],
        "expected": [[-2, 0, 2], [-2, 1, 1]],
        "case_id": 4
    },
    {
        "method": "threeSum",
        "nums": [-4, -2, -2, -2, 0, 1, 2, 2, 2, 2],
        "expected": [[-4, 2, 2], [-2, 0, 2]],
        "case_id": 5
    }
]

run_tests()
