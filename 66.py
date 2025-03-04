# 66. Plus One
#
# Given a non-empty array of digits representing a non-negative integer, increment one to the integer.
#
# The digits are stored such that the most significant digit is at the head of the list, and each element in the array is a digit.
#
# You may assume the integer does not contain any leading zeros, except the number 0 itself.
#
# Return the resulting array of digits after adding one to the integer.
#
# Constraints:
# - 1 <= digits.length <= 100
# - 0 <= digits[i] <= 9
# - digits does not contain any leading zeros, except for the number 0.


from test.test_suite import run_tests


class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        n = len(digits)

        # 从最后一位开始逐位加 1，处理进位
        for i in range(n - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0  # 处理进位

        # 如果所有位都变成了 0，说明需要在最前面加 1
        return [1] + digits


# class Solution:
#     def plusOne(self, digits: list[int]) -> list[int]:
#         return [int(x) for x in str(int("".join([str(x) for x in digits])) + 1)]


test_cases = [
    {
        "method": "plusOne",
        "digits": [1, 2, 3],
        "expected": [1, 2, 4],
        "case_id": 1
    },
    {
        "method": "plusOne",
        "digits": [9],
        "expected": [1, 0],
        "case_id": 2
    },
    {
        "method": "plusOne",
        "digits": [9, 9],
        "expected": [1, 0, 0],
        "case_id": 3
    },
    {
        "method": "plusOne",
        "digits": [1, 9, 9],
        "expected": [2, 0, 0],
        "case_id": 4
    },
    {
        "method": "plusOne",
        "digits": [0],
        "expected": [1],
        "case_id": 5
    }
]
run_tests()
