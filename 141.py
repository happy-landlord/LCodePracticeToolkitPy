# 141.py
from test.test_suite import run_tests
from libs.linked_list import ListNode


# 141. Linked List Cycle

# Given the `head` of a linked list, determine if the linked list has a cycle in it.
#
# There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the `next` pointer.
#
# Internally, `pos` is used to denote the index of the node that tail's next pointer is connected to. **Note that `pos` is not passed as a parameter**.
#
# Return `true` if there is a cycle in the linked list. Otherwise, return `false`.
#
# ### Constraints:
# - The number of nodes in the list is in the range `[0, 10^4]`.
# - `-10^5 <= Node.val <= 10^5`
# - `pos` is `-1` or a valid index in the linked list.
#
# ---
#
# ### Examples:
#
# #### Example 1:
# **Input:** head = [3,2,0,-4], pos = 1
# **Output:** true
# **Explanation:** There is a cycle in the linked list where the tail connects to the second node.
#
# #### Example 2:
# **Input:** head = [1,2], pos = 0
# **Output:** true
# **Explanation:** There is a cycle in the linked list where the tail connects to the first node.
#
# #### Example 3:
# **Input:** head = [1], pos = -1
# **Output:** false
# **Explanation:** There is no cycle in the linked list.
#

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False


test_cases = [
    {
        "method": "hasCycle",
        "head": [3, 2, 0, -4],
        "pos": 1,
        "expected": True,
        "case_id": 1
    },
    {
        "method": "hasCycle",
        "head": [1, 2],
        "pos": 0,
        "expected": True,
        "case_id": 2
    },
    {
        "method": "hasCycle",
        "head": [1],
        "pos": -1,
        "expected": False,
        "case_id": 3
    },
    {
        "method": "hasCycle",
        "head": [],
        "pos": -1,
        "expected": False,
        "case_id": 4
    },
    {
        "method": "hasCycle",
        "head": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        "pos": 4,
        "expected": True,
        "case_id": 5
    },
    {
        "method": "hasCycle",
        "head": [10, 20, 30, 40, 50],
        "pos": -1,
        "expected": False,
        "case_id": 6
    }
]

run_tests()
