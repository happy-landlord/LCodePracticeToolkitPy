# libs/tree.py

from collections import deque
from typing import Any, List, Optional, Union


class TreeNode:
    """
    Definition for a binary tree node.
    符合 LeetCode 的标准签名：
    # class TreeNode:
    #     def __init__(self, val=0, left=None, right=None):
    #         self.val = val
    #         self.left = left
    #         self.right = right
    """

    def __init__(self, val: Any = 0, left: Optional['TreeNode'] = None, right: Optional['TreeNode'] = None):
        self.val = val
        self.left = left
        self.right = right


def build_tree_from_list(values: List[Optional[Any]]) -> Optional[TreeNode]:
    """
    根据按层序遍历给定的列表构造二叉树。
    采用基于索引的遍历方式，能正确处理稀疏数组表示（例如 [1, None, 2, None, None, None, 3]）
    """
    if not values:
        return None
    root_val = values[0]
    if root_val is None:
        return None
    root = TreeNode(root_val)
    queue = deque([root])
    i = 1
    while queue and i < len(values):
        current = queue.popleft()
        # 左孩子
        if i < len(values):
            left_val = values[i]
            i += 1
            if left_val is not None:
                current.left = TreeNode(left_val)
                queue.append(current.left)
        # 右孩子
        if i < len(values):
            right_val = values[i]
            i += 1
            if right_val is not None:
                current.right = TreeNode(right_val)
                queue.append(current.right)
    return root


def tree_to_list(root: Optional[TreeNode]) -> List[Optional[Any]]:
    if not root:
        return []
    result: List[Optional[Any]] = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    return result  # 不直接移除末尾 None，交给后续处理


def find_node_by_value(root: Optional[TreeNode], val: Any) -> Optional[TreeNode]:
    """
    在二叉树中查找第一个节点，其值与 val 相等。使用深度优先搜索。
    """
    if root is None:
        return None
    if root.val == val:
        return root
    left = find_node_by_value(root.left, val)
    if left is not None:
        return left
    return find_node_by_value(root.right, val)
