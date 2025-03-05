# 100.py
from test.test_suite import run_tests

from typing import Optional
from libs.tree import TreeNode
from libs.tree import tree_to_list


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
        return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


test_cases = [
    {
        "method": "isSameTree",
        "p": [1, 2, 3],
        "q": [1, 2, 3],
        "expected": True,
        "case_id": 1,
        "description": "Identical trees with three nodes"
    },
    {
        "method": "isSameTree",
        "p": [1, 2],
        "q": [1, None, 2],
        "expected": False,
        "case_id": 2,
        "description": "Trees with different structure"
    },
    {
        "method": "isSameTree",
        "p": [1, 2, 1],
        "q": [1, 1, 2],
        "expected": False,
        "case_id": 3,
        "description": "Trees with same length but different values"
    },
    {
        "method": "isSameTree",
        "p": [],
        "q": [],
        "expected": True,
        "case_id": 4,
        "description": "Empty trees are considered the same"
    },
    {
        "method": "isSameTree",
        "p": [1],
        "q": [1],
        "expected": True,
        "case_id": 5,
        "description": "Single node trees with same value"
    },
    {
        "method": "isSameTree",
        "p": [1],
        "q": [2],
        "expected": False,
        "case_id": 6,
        "description": "Single node trees with different values"
    },
    {
        "method": "isSameTree",
        "p": [1, 2, 3, 4, 5],
        "q": [1, 2, 3, 4, 5],
        "expected": True,
        "case_id": 7,
        "description": "Larger identical trees with multiple levels"
    }
]

run_tests()
