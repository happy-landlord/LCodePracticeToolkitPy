from test.test_suite import run_tests
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # 定义搜索范围的左右边界
        left, right = 0, len(nums) - 1
        # 当搜索范围有效时继续二分
        while left <= right:
            # 计算中间位置，避免溢出
            middle = left + (right - left) // 2
            # 找到目标直接返回
            if nums[middle] == target:
                return middle
            # 目标在右半部分，缩小左边界
            elif nums[middle] < target:
                left = middle + 1
            # 目标在左半部分，缩小右边界
            else:
                right = middle - 1
        # 未找到目标，返回 -1
        return -1


test_cases = [
    {
        "method": "search",
        "nums": [-1, 0, 3, 5, 9, 12],
        "target": 9,
        "expected": 4,
        "case_id": 1
    },
    {
        "method": "search",
        "nums": [-1, 0, 3, 5, 9, 12],
        "target": 2,
        "expected": -1,
        "case_id": 2
    },
    {
        "method": "search",
        "nums": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        "target": 10,
        "expected": 9,
        "case_id": 3
    },
    {
        "method": "search",
        "nums": [5],
        "target": 5,
        "expected": 0,
        "case_id": 4
    },
    {
        "method": "search",
        "nums": [1, 3, 5, 7, 9],
        "target": 1,
        "expected": 0,
        "case_id": 5
    },
    {
        "method": "search",
        "nums": [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],
        "target": 7,
        "expected": -1,
        "case_id": 6
    }
]

run_tests()
