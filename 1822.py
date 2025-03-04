# 1822. Sign of the Product of an Array

# There is a function signFunc(x) that returns:
# - 1 if x is positive.
# - -1 if x is negative.
# - 0 if x is zero.
#
# You are given an integer array nums. Let product be the product of all the values in the array nums.
#
# Return signFunc(product).
#
# Example 1:
# Input: nums = [-1,-2,-3,-4,3,2,1]
# Output: 1
# Explanation: The product of all values in the array is 144, and signFunc(144) = 1.
#
# Example 2:
# Input: nums = [1,5,0,2,-3]
# Output: 0
# Explanation: The product of all values in the array is 0, and signFunc(0) = 0.
#
# Example 3:
# Input: nums = [-1,1,-1,1,-1]
# Output: -1
# Explanation: The product of all values in the array is -1, and signFunc(-1) = -1.
#
# Constraints:
# - 1 <= nums.length <= 1000
# - -100 <= nums[i] <= 100
#
#


from test.test_suite import run_tests


class Solution:
    def arraySign(self, nums: list[int]) -> int:
        final_sign = 1
        for num in nums:
            if num == 0: return 0
            if num < 0: final_sign = -1 * final_sign
        return -1 if final_sign == -1 else 1


test_cases = [
    {
        "method": "arraySign",
        "nums": [-1, -2, -3, -4, 3, 2, 1],
        "expected": 1,
        "case_id": 1
    },
    {
        "method": "arraySign",
        "nums": [1, 5, 0, 2, -3],
        "expected": 0,
        "case_id": 2
    },
    {
        "method": "arraySign",
        "nums": [-1, 1, -1, 1, -1],
        "expected": -1,
        "case_id": 3
    },
    {
        "method": "arraySign",
        "nums": [0, -1, 1, -1, 1, -1],
        "expected": 0,
        "case_id": 4
    },
    {
        "method": "arraySign",
        "nums": [-5],
        "expected": -1,
        "case_id": 5
    }
]

run_tests()
