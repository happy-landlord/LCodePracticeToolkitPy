# 153.py
from pprint import pprint

from test.test_suite import run_tests


class Solution:
    def findMin(self, nums: list[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right:  # 注意这里用 <
            mid = left + (right - left) // 2
            if nums[mid] > nums[right]:
                left = mid + 1  # 最小值在右半部分
            else:
                right = mid  # 最小值在左半部分或 mid
        return nums[left]  # left == right 时即为最小值


test_cases = [
    {
        "method": "findMin",
        "nums": [3, 4, 5, 1, 2],
        "expected": 1,
        "case_id": 1
    },
    {
        "method": "findMin",
        "nums": [4, 5, 6, 7, 0, 1, 2],
        "expected": 0,
        "case_id": 2
    },
    {
        "method": "findMin",
        "nums": [11, 13, 15, 17],
        "expected": 11,
        "case_id": 3
    },
    {
        "method": "findMin",
        "nums": [2, 1],
        "expected": 1,
        "case_id": 4
    },
    {
        "method": "findMin",
        "nums": [1],
        "expected": 1,
        "case_id": 5
    },
    {
        "method": "findMin",
        "nums": [10, 20, 30, 40, 50, 5, 7],
        "expected": 5,
        "case_id": 6
    }
]

run_tests()
