# 143.py
from test.test_suite import run_tests

from typing import Optional
from libs.linked_list import ListNode

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        pass


test_cases = [
    {
        "method": "reorderList",
        "head": [1, 2, 3, 4],
        "expected": [1, 4, 2, 3],
        "case_id": 1
    },
    {
        "method": "reorderList",
        "head": [1, 2, 3, 4, 5],
        "expected": [1, 5, 2, 4, 3],
        "case_id": 2
    },
    {
        "method": "reorderList",
        "head": [1, 2],
        "expected": [1, 2],
        "case_id": 3
    },
    {
        "method": "reorderList",
        "head": [1],
        "expected": [1],
        "case_id": 4
    },
    {
        "method": "reorderList",
        "head": [10, 20, 30, 40, 50, 60],
        "expected": [10, 60, 20, 50, 30, 40],
        "case_id": 5
    }
]

run_tests()
