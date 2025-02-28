# 389.py
from collections import Counter
from test.test_suite import run_tests


class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        c_s = Counter(s)
        c_t = Counter(t)
        return list((c_t - c_s).keys())[0]


test_cases = [
    {
        "method": "findTheDifference",
        "s": "abcd",
        "t": "abcde",
        "expected": "e",
        "case_id": 1
    },
    {
        "method": "findTheDifference",
        "s": "",
        "t": "y",
        "expected": "y",
        "case_id": 2
    },
    {
        "method": "findTheDifference",
        "s": "a",
        "t": "aa",
        "expected": "a",
        "case_id": 3
    },
    {
        "method": "findTheDifference",
        "s": "ae",
        "t": "aea",
        "expected": "a",
        "case_id": 4
    }
]

run_tests()
