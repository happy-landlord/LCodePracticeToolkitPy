# 1.py
from test.test_suite import run_tests


class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hashed = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in hashed: return sorted([i, hashed[diff]])
            hashed[num] = i
        return []


test_cases = [
    {
        "method": "twoSum",
        "nums": [2, 7, 11, 15],
        "target": 9,
        "expected": [0, 1],
        "case_id": 1
    },
    {
        "method": "twoSum",
        "nums": [3, 2, 4],
        "target": 6,
        "expected": [1, 2],
        "case_id": 2
    },
    {
        "method": "twoSum",
        "nums": [3, 3],
        "target": 6,
        "expected": [0, 1],
        "case_id": 3
    },
    {
        "method": "twoSum",
        "nums": [1, 5, 3, 6],
        "target": 9,
        "expected": [2, 3],
        "case_id": 4
    },
    {
        "method": "twoSum",
        "nums": [-3, 4, 3, 90],
        "target": 0,
        "expected": [0, 2],
        "case_id": 5
    }
]

run_tests()
