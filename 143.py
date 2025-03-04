from test.test_suite import run_tests
from typing import Optional
from libs.linked_list import ListNode


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return

        # Step 1: Find the middle
        slow = fast = head
        prev = None
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        prev.next = None  # Split into two lists

        # Step 2: Reverse the second half
        second = slow
        prev = None
        while second:
            next_node = second.next
            second.next = prev
            prev = second
            second = next_node

        # Step 3: Merge the two halves
        first = head
        second = prev
        while first and second:  # Stop when either list is exhausted
            tmp1, tmp2 = first.next, second.next
            first.next = second
            if tmp1:
                second.next = tmp1
            first, second = tmp1, tmp2


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
