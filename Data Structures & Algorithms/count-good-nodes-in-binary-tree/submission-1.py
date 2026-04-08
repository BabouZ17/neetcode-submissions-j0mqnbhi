# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        queue = deque([(root, root.val)])

        res = 0

        while queue:
            node, curr_max = queue.popleft()

            if node.val >= curr_max:
                res += 1

            curr_max = max(curr_max, node.val)
            if node.left is not None:
                queue.append((node.left, curr_max))
            if node.right is not None:
                queue.append((node.right, curr_max))
        return res