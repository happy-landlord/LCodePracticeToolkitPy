# 142.py
from test.test_suite import run_tests
from libs.linked_list import ListNode


class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return None

        # Step 1: Detect cycle using fast and slow pointers
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        else:
            return None  # No cycle

        # Step 2: Find cycle entry
        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next
        return slow


test_cases = [
    {
        "method": "detectCycle",
        "head": [3, 2, 0, -4],  # The linked list structure should be built before testing
        "pos": 1,  # The cycle connects to node index 1
        "expected": 1,  # The function should return the node at index 1
        "case_id": 1
    },
    {
        "method": "detectCycle",
        "head": [1, 2],
        "pos": 0,  # The cycle connects to node index 0
        "expected": 0,  # The function should return the node at index 0
        "case_id": 2
    },
    {
        "method": "detectCycle",
        "head": [1],
        "pos": -1,  # No cycle
        "expected": None,  # The function should return None
        "case_id": 3
    },
    {
        "method": "detectCycle",
        "head": [1, 2, 3, 4, 5],
        "pos": -1,  # No cycle
        "expected": None,  # The function should return None
        "case_id": 4
    },
    {
        "method": "detectCycle",
        "head": [1, 2, 3, 4, 5, 6],
        "pos": 3,  # The cycle connects to node index 3
        "expected": 3,  # The function should return the node at index 3
        "case_id": 5
    },
    {
        "method": "detectCycle",
        "head": [1, 2, 3],
        "pos": 2,  # The cycle connects to node index 2
        "expected": 2,  # The function should return the node at index 2
        "case_id": 6
    }
]

run_tests()
