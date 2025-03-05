# 98.py
from test.test_suite import run_tests

from typing import Optional
from libs.tree import TreeNode, tree_to_list


class Solution:
    # 方法 1：递归 DFS（上下界法）| 范围检查：为每个节点维护一个有效值范围，递归验证。
    # O(n)（每个节点只访问一次）
    # def isValidBST(self, root: Optional[TreeNode]) -> bool:
    #
    #     def validate(node, low, high):
    #         if not node:
    #             return True
    #
    #         if not (low < node.val < high):
    #             return False
    #
    #         return validate(node.left, low, node.val) and validate(node.right, node.val, high)
    #
    #     return validate(root, float('-inf'), float('inf'))

    # 方法 2：递归中序遍历：利用二叉搜索树中序遍历结果严格递增的性质：在中序遍历过程中记录上一个访问的节点值，如果当前节点值不大于前一个值，则不是 BST。
    # O(n)
    # def _inorder_check(self, node: Optional[TreeNode], prev: list[float]) -> bool:
    #     # 空节点是有效的
    #     if not node:
    #         return True
    #
    #     # 先检查左子树
    #     if not self._inorder_check(node.left, prev):
    #         return False
    #
    #     # 当前节点必须大于前一个值
    #     if node.val <= prev[0]:
    #         return False
    #
    #     # 更新前一个值为当前值
    #     prev[0] = node.val
    #
    #     # 检查右子树
    #     return self._inorder_check(node.right, prev)
    #
    # def isValidBST(self, root: Optional[TreeNode]) -> bool:
    #     # 中序遍历检查 BST：每个节点值必须大于前一个访问的值
    #     return self._inorder_check(root, [float('-inf')])  # 用列表传递可变状态

    # def isValidBST(self, root: Optional[TreeNode]) -> bool:
    #     if not root:
    #         return True
    #
    #     stack = []
    #     prev = float('-inf')
    #     node = root
    #
    #     while node or stack:
    #         # 先往左走到尽头，把沿途节点存起来
    #         if node:
    #             stack.append(node)
    #             node = node.left
    #         # 回头检查一个节点，再往右走
    #         else:
    #             node = stack.pop()
    #             if node.val <= prev:  # 房间号必须递增
    #                 return False
    #             prev = node.val  # 记住这次的房间号
    #             node = node.right  # 转向右路
    #
    #     return True

    # def isValidBST(self, root: Optional[TreeNode]) -> bool:
    #
    #     if not root:
    #         return True
    #
    #     rooms_to_check = [(root, float('-inf'), float('inf'))]
    #
    #     while rooms_to_check:
    #
    #         room, min_key, max_key = rooms_to_check.pop()
    #
    #         if not room:
    #             continue
    #
    #         if not (min_key < room.val < max_key):
    #             return False
    #
    #         rooms_to_check.append((room.left, min_key, room.val))
    #         rooms_to_check.append((room.right, room.val, max_key))
    #
    #     return True

    # def isValidBST(self, root: Optional[TreeNode]) -> bool:
    #     if not root:
    #         return True
    #
    #     # 中序遍历收集值到列表
    #     stack = []
    #     values = []
    #     node = root
    #     while node or stack:
    #         if node:
    #             stack.append(node)
    #             node = node.left
    #         else:
    #             node = stack.pop()
    #             values.append(node.val)
    #             node = node.right
    #
    #     # 检查是否严格升序
    #     for i in range(1, len(values)):
    #         if values[i] <= values[i - 1]:
    #             return False
    #     return True
    #
    # 优化为“边收集边检查”，避免第二次遍历：
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        stack = []
        values = []
        node = root
        while node or stack:
            if node:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                # 边收集边检查
                if values and node.val <= values[-1]:
                    return False
                values.append(node.val)
                node = node.right
        return True


test_cases = [
    {
        "method": "isValidBST",
        "root": [2, 1, 3],
        "expected": True,
        "case_id": 1,
        "description": "Standard valid BST"
    },
    {
        "method": "isValidBST",
        "root": [5, 1, 4, None, None, 3, 6],
        "expected": False,
        "case_id": 2,
        "description": "Invalid BST: Right subtree violates BST property"
    },
    {
        "method": "isValidBST",
        "root": [],
        "expected": True,
        "case_id": 3,
        "description": "Edge case: Empty tree (considered valid BST)"
    },
    {
        "method": "isValidBST",
        "root": [1],
        "expected": True,
        "case_id": 4,
        "description": "Edge case: Single node tree"
    },
    {
        "method": "isValidBST",
        "root": [2, 2, 3],
        "expected": False,
        "case_id": 5,
        "description": "Edge case: Tree with duplicate value in left subtree"
    },
    {
        "method": "isValidBST",
        "root": [10, 5, 15, None, None, 6, 20],
        "expected": False,
        "case_id": 6,
        "description": "Invalid BST: Subtree of right node violates BST property"
    },
    {
        "method": "isValidBST",
        "root": [10, 5, 15, 2, 7, 12, 20],
        "expected": True,
        "case_id": 7,
        "description": "Complete valid BST with multiple levels"
    }
]

run_tests()
