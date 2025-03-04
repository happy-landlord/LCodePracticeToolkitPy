# https://leetcode.com/problems/container-with-most-water/description/

from test.test_suite import run_tests


class Solution:
    def maxArea(self, height: list[int]) -> int:
        max_area = 0
        left, right = 0, len(height) - 1
        while left < right:
            max_area = max(max_area, min(height[left], height[right]) * (right - left))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area


test_cases = [
    {
        "method": "maxArea",
        "height": [1, 8, 6, 2, 5, 4, 8, 3, 7],
        "expected": 49,
        "case_id": 1
    },
    {
        "method": "maxArea",
        "height": [1, 1],
        "expected": 1,
        "case_id": 2
    },
    {
        "method": "maxArea",
        "height": [4, 3, 2, 1, 4],
        "expected": 16,
        "case_id": 3
    },
    {
        "method": "maxArea",
        "height": [1, 2, 1],
        "expected": 2,
        "case_id": 4
    },
    {
        "method": "maxArea",
        "height": [2, 3, 4, 5, 18, 17, 6],
        "expected": 17,
        "case_id": 5
    }
]

run_tests()
