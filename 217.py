# 217.py
from test.test_suite import run_tests


class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        return len(set(nums)) < len(nums)


test_cases = [
    {
        "method": "containsDuplicate",
        "nums": [1, 2, 3, 1],
        "expected": True,
        "case_id": 1
    },
    {
        "method": "containsDuplicate",
        "nums": [1, 2, 3, 4],
        "expected": False,
        "case_id": 2
    },
    {
        "method": "containsDuplicate",
        "nums": [1, 1, 1, 3, 3, 4, 3, 2, 4, 2],
        "expected": True,
        "case_id": 3
    },
    {
        "method": "containsDuplicate",
        "nums": [0],
        "expected": False,
        "case_id": 4
    },
    {
        "method": "containsDuplicate",
        "nums": [10 ** 9, -10 ** 9, 0, 10 ** 9],
        "expected": True,
        "case_id": 5
    }
]

run_tests()
