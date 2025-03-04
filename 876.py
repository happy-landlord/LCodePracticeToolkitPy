# 876.py
from test.test_suite import run_tests

from libs.linked_list import ListNode


# 画示意图时，把尾部的None也画出来，一目了然
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow


test_cases = [
    {
        "method": "middleNode",
        "head": [1, 2, 3, 4, 5],
        "expected": [3, 4, 5],
        "case_id": 1
    },
    {
        "method": "middleNode",
        "head": [1, 2, 3, 4, 5, 6],
        "expected": [4, 5, 6],
        "case_id": 2
    },
    {
        "method": "middleNode",
        "head": [1],
        "expected": [1],
        "case_id": 3
    },
    {
        "method": "middleNode",
        "head": [1, 2],
        "expected": [2],
        "case_id": 4
    },
    {
        "method": "middleNode",
        "head": [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],
        "expected": [60, 70, 80, 90, 100],
        "case_id": 5
    },
    {
        "method": "middleNode",
        "head": [7, 14, 21, 28, 35, 42, 49],
        "expected": [28, 35, 42, 49],
        "case_id": 6
    }
]

run_tests()
