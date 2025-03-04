# 283.py
from test.test_suite import run_tests


class Solution:
    def moveZeroes(self, nums: [int]) -> None:
        index = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[index] = nums[i]
                index += 1
        # 填充剩下的位置为零
        for i in range(index, len(nums)):
            nums[i] = 0
        return nums

test_cases = [
    {
        "method": "moveZeroes",
        "nums": [0, 1, 0, 3, 12],
        "expected": [1, 3, 12, 0, 0],
        "case_id": 1
    },
    {
        "method": "moveZeroes",
        "nums": [0],
        "expected": [0],
        "case_id": 2
    },
    {
        "method": "moveZeroes",
        "nums": [1, 2, 3, 4, 5],
        "expected": [1, 2, 3, 4, 5],
        "case_id": 3
    },
    {
        "method": "moveZeroes",
        "nums": [0, 0, 0, 0, 1],
        "expected": [1, 0, 0, 0, 0],
        "case_id": 4
    },
    {
        "method": "moveZeroes",
        "nums": [1, 0, 1, 0, 1, 0],
        "expected": [1, 1, 1, 0, 0, 0],
        "case_id": 5
    },
    {
        "method": "moveZeroes",
        "nums": [0, 0, 0, 0, 0],
        "expected": [0, 0, 0, 0, 0],
        "case_id": 6
    },
    {
        "method": "moveZeroes",
        "nums": [-1, 0, 5, -3, 0, 10],
        "expected": [-1, 5, -3, 10, 0, 0],
        "case_id": 7
    }
]

run_tests()
