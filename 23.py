from test.test_suite import run_tests
from typing import List, Optional
from libs.linked_list import ListNode
import heapq


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None

        # 将 Python 列表转换为 ListNode 链表
        node_lists = []
        for sublist in lists:
            if isinstance(sublist, list):  # 输入是 Python 列表
                node_lists.append(ListNode.from_list(sublist) if sublist else None)
            else:  # 输入已是 ListNode
                node_lists.append(sublist)

        # 初始化最小堆
        pq = []
        for i, lst in enumerate(node_lists):
            if lst:
                heapq.heappush(pq, (lst.val, i, lst))

        if not pq:
            return None

        # 合并链表
        dummy = ListNode(0)
        curr = dummy
        while pq:
            val, i, node = heapq.heappop(pq)
            curr.next = node
            curr = curr.next
            if node.next:
                heapq.heappush(pq, (node.next.val, i, node.next))

        return dummy.next


test_cases = [
    {
        "method": "mergeKLists",
        "lists": [[1, 4, 5], [1, 3, 4], [2, 6]],
        "expected": [1, 1, 2, 3, 4, 4, 5, 6],
        "case_id": 1
    },
    {
        "method": "mergeKLists",
        "lists": [],
        "expected": [],
        "case_id": 2
    },
    {
        "method": "mergeKLists",
        "lists": [[]],
        "expected": [],
        "case_id": 3
    },
    {
        "method": "mergeKLists",
        "lists": [[-10, -9, -9, -3, -1, -1, 0], [-5], [4], [-8]],
        "expected": [-10, -9, -9, -8, -5, -3, -1, -1, 0, 4],
        "case_id": 4
    },
    {
        "method": "mergeKLists",
        "lists": [[1, 3, 5, 7], [2, 4, 6, 8, 10], [9, 11, 13]],
        "expected": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13],
        "case_id": 5
    },
    {
        "method": "mergeKLists",
        "lists": [[1], [0], [2], [5], [4], [3]],
        "expected": [0, 1, 2, 3, 4, 5],
        "case_id": 6
    }
]

run_tests()
