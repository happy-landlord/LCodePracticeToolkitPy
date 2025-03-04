# 206.py
import math
from typing import Optional
from collections import deque

from libs.linked_list import ListNode
from test.test_suite import run_tests


# class Solution:
#     def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         stack = deque()
#         current = head
#
#         while current:
#             stack.append(current)
#             current = current.next
#
#         dummy_head = ListNode(math.inf)
#         current = dummy_head
#
#         while len(stack):
#             current.next = stack.pop()
#             current = current.next
#
#         current.next = None
#         return dummy_head.next


# 最优解：
# 火车掉头的比喻
# 想象一个单向火车（链表），每节车厢只能指向后面一节（next指针）。现在要把整列火车掉头，让最后一节变成头，第一节变成尾。我们用三个工作人员来操作：
# “存next，指prev，往前挪”
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None  # 前车厢，初始为空（掉头后尾巴是null）
        curr = head  # 当前车厢，从头开始

        while curr:  # 只要还有车厢没处理
            next = curr.next  # 1. 存next：记住下一节车厢
            curr.next = prev  # 2. 指prev：掉转当前车厢方向
            prev = curr  # 3. 往前挪：三人往前走一步
            curr = next  # 前车厢变当前，当前跳到下一节

        return prev  # 返回新的头（最后一节车厢）


test_cases = [
    {
        "method": "reverseList",
        "head": [1, 2, 3, 4, 5],
        "expected": [5, 4, 3, 2, 1],
        "case_id": 1
    },
    {
        "method": "reverseList",
        "head": [1, 2],
        "expected": [2, 1],
        "case_id": 2
    },
    {
        "method": "reverseList",
        "head": [],
        "expected": [],
        "case_id": 3
    },
    {
        "method": "reverseList",
        "head": [5],
        "expected": [5],
        "case_id": 4
    },
    {
        "method": "reverseList",
        "head": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        "expected": [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
        "case_id": 5
    }
]
run_tests()
