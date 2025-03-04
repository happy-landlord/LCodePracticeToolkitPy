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
        """
        使用Floyd's龟兔算法（快慢指针）检测链表是否有环

        时间复杂度: O(n)，其中n是链表中的节点数
        空间复杂度: O(1)，只使用两个指针

        Args:
            head: 链表的头节点

        Returns:
            bool: 如果链表中存在环，则返回True；否则返回False
        """
        # 空链表或只有一个节点的链表不可能有环
        if not head or not head.next:
            return False

        # 设置慢指针和快指针
        slow = head
        fast = head

        # 快指针每次走两步，慢指针每次走一步
        # 如果存在环，快指针最终会追上慢指针
        while fast and fast.next:
            slow = slow.next  # 慢指针走一步
            fast = fast.next.next  # 快指针走两步

            # 如果两个指针相遇，说明存在环
            if slow == fast:
                return True

        # 如果快指针到达链表末尾，说明没有环
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
