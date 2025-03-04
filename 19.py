from test.test_suite import run_tests
from typing import Optional
from libs.linked_list import ListNode

from test.test_suite import run_tests
from typing import Optional
from libs.linked_list import ListNode


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> ListNode:
        if not head:
            return None

        dummy = ListNode(0)
        dummy.next = head
        fast = slow = dummy

        for _ in range(n):
            fast = fast.next

        while fast.next:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next
        return dummy.next


test_cases = [
    {
        "method": "removeNthFromEnd",
        "head": [1, 2, 3, 4, 5],
        "n": 2,
        "expected": [1, 2, 3, 5],
        "case_id": 1
    },
    {
        "method": "removeNthFromEnd",
        "head": [1],
        "n": 1,
        "expected": [],
        "case_id": 2
    },
    {
        "method": "removeNthFromEnd",
        "head": [1, 2],
        "n": 1,
        "expected": [1],
        "case_id": 3
    }
]

run_tests()
