# 167.py
from test.test_suite import run_tests


class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        low, high = 0, len(numbers) - 1
        # 题目中提示了：`where 1 <= index1 < index2 <= numbers.length.`
        while low < high:
            summary = numbers[low] + numbers[high]
            if summary == target: return [low + 1, high + 1]

            if summary < target:
                low += 1
            else:
                high -= 1


test_cases = [
    {
        "method": "twoSum",
        "numbers": [2, 7, 11, 15],
        "target": 9,
        "expected": [1, 2],
        "case_id": 1
    },
    {
        "method": "twoSum",
        "numbers": [2, 3, 4],
        "target": 6,
        "expected": [1, 3],
        "case_id": 2
    },
    {
        "method": "twoSum",
        "numbers": [-1, 0],
        "target": -1,
        "expected": [1, 2],
        "case_id": 3
    },
    {
        "method": "twoSum",
        "numbers": [1, 2, 3, 4, 4, 9, 56, 90],
        "target": 8,
        "expected": [4, 5],
        "case_id": 4
    },
    {
        "method": "twoSum",
        "numbers": [5, 25, 75],
        "target": 100,
        "expected": [2, 3],
        "case_id": 5
    }
]

run_tests()
