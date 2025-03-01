# 21.py

from typing import Optional

from libs.linked_list import ListNode
from test.test_suite import run_tests


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        current = dummy
        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
        # 链接剩余部分（此时只有一个非空）
        current.next = list1 if list1 else list2
        return dummy.next


test_cases = [
    {
        "method": "mergeTwoLists",
        "list1": [1, 2, 4],
        "list2": [1, 3, 4],
        "expected": [1, 1, 2, 3, 4, 4],
        "case_id": 1
    },
    {
        "method": "mergeTwoLists",
        "list1": [],
        "list2": [],
        "expected": [],
        "case_id": 2
    },
    {
        "method": "mergeTwoLists",
        "list1": [],
        "list2": [0],
        "expected": [0],
        "case_id": 3
    },
    {
        "method": "mergeTwoLists",
        "list1": [5],
        "list2": [1, 2, 3, 4, 6],
        "expected": [1, 2, 3, 4, 5, 6],
        "case_id": 4
    },
    {
        "method": "mergeTwoLists",
        "list1": [-10, -5, 3, 7],
        "list2": [-6, -4, 2, 8, 9],
        "expected": [-10, -6, -5, -4, 2, 3, 7, 8, 9],
        "case_id": 5
    }
]

run_tests()
