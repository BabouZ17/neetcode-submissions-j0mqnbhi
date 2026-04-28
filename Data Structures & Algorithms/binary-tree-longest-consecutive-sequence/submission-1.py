# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        if not root: return 0

        res = 1

        queue = deque()
        queue.append((root, None, 0))

        while queue:
            node, parent_val, path = queue.popleft()

            if parent_val is None or node.val == parent_val + 1:
                path += 1
            else:
                path = 1

            res = max(res, path)

            if node.left:
                queue.append((node.left, node.val, path))
            if node.right:
                queue.append((node.right, node.val, path))
        return res