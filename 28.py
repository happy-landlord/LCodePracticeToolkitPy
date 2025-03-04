# 28. Implement strStr()
#
# Implement the strStr() function.
#
# Given two strings haystack and needle, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
#
# Clarification:
# 	•	If needle is an empty string, return 0.
#
# Constraints:
# 	•	1 <= haystack.length <= 10^4
# 	•	0 <= needle.length <= 10^4
# 	•	haystack and needle consist of only lowercase English characters.
#
# Example 1:
#
# Input: haystack = "hello", needle = "ll"
# Output: 2
#
# Example 2:
#
# Input: haystack = "aaaaa", needle = "bba"
# Output: -1
#
# Example 3:
#
# Input: haystack = "", needle = ""
# Output: 0
#
# Example 4:
#
# Input: haystack = "mississippi", needle = "issip"
# Output: 4

from test.test_suite import run_tests


# 初稿问题：
# 考虑但没处理越界问题
# 没用Python的String切片写法
# enumerate的参数搞反了

# class Solution:
#     def strStr(self, haystack: str, needle: str) -> int:
#         if needle == '': return 0
#
#         n_len = len(needle)
#         h_len = len(haystack)
#
#         if n_len > h_len: return -1
#
#         for i, s in enumerate(haystack):
#             if s == needle[0] and i + n_len <= h_len:  # 确保不会越界
#                 flag = True
#                 for j in range(n_len):
#                     if needle[j] != haystack[i + j]:
#                         flag = False
#                         break
#                 if flag: return i
#
#         return -1

# 标准暴力解
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle: return 0

        n, m = len(haystack), len(needle)
        if m > n: return -1

        for i in range(n):
            if i + m <= n and haystack[i:i + m] == needle:
                return i

        return -1


test_cases = [
    {
        "method": "strStr",
        "haystack": "hello",
        "needle": "ll",
        "expected": 2,
        "case_id": 1
    },
    {
        "method": "strStr",
        "haystack": "aaaaa",
        "needle": "bba",
        "expected": -1,
        "case_id": 2
    },
    {
        "method": "strStr",
        "haystack": "",
        "needle": "",
        "expected": 0,
        "case_id": 3
    },
    {
        "method": "strStr",
        "haystack": "mississippi",
        "needle": "issip",
        "expected": 4,
        "case_id": 4
    },
    {
        "method": "strStr",
        "haystack": "abcde",
        "needle": "cde",
        "expected": 2,
        "case_id": 5
    },
    {
        "method": "strStr",
        "haystack": "hello",
        "needle": "ooo",  # needle比haystack长，越界
        "expected": -1,
        "case_id": 6
    },
    {
        "method": "strStr",
        "haystack": "abcde",
        "needle": "def",  # 后面部分不足以匹配整个needle
        "expected": -1,
        "case_id": 7
    },
    {
        "method": "strStr",
        "haystack": "abcde",
        "needle": "de",  # 可以匹配到，返回2
        "expected": 3,
        "case_id": 8
    },
    {
        "method": "strStr",
        "haystack": "abcdef",
        "needle": "efg",  # needle比剩余部分长，越界
        "expected": -1,
        "case_id": 9
    },
    {
        "method": "strStr",
        "haystack": "ab",
        "needle": "abc",  # needle比haystack长，越界
        "expected": -1,
        "case_id": 10
    }
]

run_tests()
