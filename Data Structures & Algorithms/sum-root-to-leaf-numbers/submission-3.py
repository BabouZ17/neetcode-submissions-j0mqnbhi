# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        queue = deque([(root, root.val)])
        total = 0
        while queue:
            node, curr = queue.popleft()
            if node.left is None and node.right is None:
                total += curr
            if node.left is not None:
                queue.append((node.left, curr * 10 + node.left.val))
            if node.right is not None:
                queue.append((node.right, curr * 10 + node.right.val))
        return total