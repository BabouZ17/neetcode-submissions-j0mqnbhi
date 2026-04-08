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

        queue = deque([(root, [root.val])])
        total = 0

        while queue:
            node, curr_total = queue.popleft()
            if node.left is None and node.right is None:
                total += int("".join([str(val) for val in curr_total]))
            if node.left:
                val = curr_total[:]
                val.append(node.left.val)
                queue.append((node.left, val))
            if node.right:
                val = curr_total[:]
                val.append(node.right.val)
                queue.append((node.right, val))
        return total