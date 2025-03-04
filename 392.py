# 392.py
from test.test_suite import run_tests


# 392. Is Subsequence

# Given two strings `s` and `t`, return `true` if `s` is a subsequence of `t`, or `false` otherwise.
#
# A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., `"ace"` is a subsequence of `"abcde"` while `"aec"` is not).
#
# Constraints:
# - 0 <= s.length <= 100
# - 0 <= t.length <= 10^4
# - `s` and `t` consist only of lowercase English letters.
#
# **Follow up:** If there are lots of incoming `s`, say s1, s2, ..., sk where k >= 10^9, and you want to check one by one to see if `t` has its subsequence. In this scenario, how would you change your code?


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        p1, p2 = 0, 0
        while p1 < len(s) and p2 < len(t):
            if s[p1] == t[p2]:
                p1 += 1
            p2 += 1
        return p1 == len(s)


test_cases = [
    {
        "method": "isSubsequence",
        "s": "abc",
        "t": "ahbgdc",
        "expected": True,
        "case_id": 1
    },
    {
        "method": "isSubsequence",
        "s": "axc",
        "t": "ahbgdc",
        "expected": False,
        "case_id": 2
    },
    {
        "method": "isSubsequence",
        "s": "",
        "t": "ahbgdc",
        "expected": True,
        "case_id": 3
    },
    {
        "method": "isSubsequence",
        "s": "acb",
        "t": "ahbgdc",
        "expected": False,
        "case_id": 4
    },
    {
        "method": "isSubsequence",
        "s": "abcde",
        "t": "abcde",
        "expected": True,
        "case_id": 5
    }
]

run_tests()
