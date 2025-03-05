Provide complete information about LeetCode problem #{problem_number}. Please include:

1. The original problem statement with all details (description, constraints, examples);
2. A Python v3.13.2 code template with the class Solution and method signature (empty function body);
3. At least 6 test cases (any numeric values have been carefully verified to ensure accuracy & at least 3 of these test
   cases are edge cases) in the structured format showed below;

## Special Instructions:

- If the problem involves a Tree data structure, add the import statement `from libs.tree import TreeNode` before the
  `class Solution:`
- If the problem involves a Linked List data structure, add the import statement `from libs.linked_list import ListNode`
  before the `class Solution:`

## Example Output Format

For reference, here's how the output should look for LeetCode problem #226:

```
# 226. Invert Binary Tree

Given the `root` of a binary tree, invert the tree, and return its root.

### Constraints:
- The number of nodes in the tree is in the range `[0, 100]`.
- `-100 <= Node.val <= 100`

### Example 1:
Input: root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]

### Example 2:
Input: root = [2,1,3]
Output: [2,3,1]

### Example 3:
Input: root = []
Output: []

```python
from typing import Optional
from typing import Optional
from libs.tree import TreeNode

# LeetCode的TreeNode实现是标准的可变对象
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        pass
        

test_cases = [
    {
        "method": "invertTree",
        "root": [4, 2, 7, 1, 3, 6, 9],
        "expected": [4, 7, 2, 9, 6, 3, 1],
        "case_id": 1,
        "description": "Standard balanced binary tree"
    }, {
        "method": "invertTree",
        "root": [2, 1, 3],
        "expected": [2, 3, 1],
        "case_id": 2,
        "description": "Small binary tree with three nodes"
    }, {
        "method": "invertTree",
        "root": [],
        "expected": [],
        "case_id": 3,
        "description": "Empty tree"
    }, {
        "method": "invertTree",
        "root": [1],
        "expected": [1],
        "case_id": 4,
        "description": "Single node tree"
    }, {
        "method": "invertTree",
        "root": [1, 2],
        "expected": [1, None, 2],
        "case_id": 5,
        "description": "Tree with only left child"
    }, {
        "method": "invertTree",
        "root": [1, None, 2],
        "expected": [1, 2, None],
        "case_id": 6,
        "description": "Tree with only right child"
    }, {
        "method": "invertTree",
        "root": [1, 2, 3, 4, 5, 6, 7],
        "expected": [1, 3, 2, 7, 6, 5, 4],
        "case_id": 7,
        "description": "Complete binary tree with multiple levels"
    }
]
```

Please provide the complete information for LeetCode problem #{problem_number} following this format.