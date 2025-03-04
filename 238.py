# 238.py
from test.test_suite import run_tests


class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        answer = [1] * n

        # 计算左侧乘积
        left_product = 1
        for i in range(n):
            answer[i] = left_product
            left_product *= nums[i]

        # 计算右侧乘积，同时更新 `answer`
        right_product = 1
        for i in range(n - 1, -1, -1):
            answer[i] *= right_product
            right_product *= nums[i]

        return answer


test_cases = [
    {
        "method": "productExceptSelf",
        "nums": [1, 2, 3, 4],
        "expected": [24, 12, 8, 6],
        "case_id": 1
    },
    {
        "method": "productExceptSelf",
        "nums": [-1, 1, 0, -3, 3],
        "expected": [0, 0, 9, 0, 0],
        "case_id": 2
    },
    {
        "method": "productExceptSelf",
        "nums": [5, 2, 3, 0, 1],
        "expected": [0, 0, 0, 30, 0],
        "case_id": 3
    },
    {
        "method": "productExceptSelf",
        "nums": [4, 3, 2, 1, 2],
        "expected": [12, 16, 24, 48, 24],
        "case_id": 4
    },
    {
        "method": "productExceptSelf",
        "nums": [1, 2],
        "expected": [2, 1],
        "case_id": 5
    }
]

run_tests()
