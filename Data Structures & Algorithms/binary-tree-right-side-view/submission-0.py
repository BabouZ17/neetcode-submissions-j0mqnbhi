# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        queue = deque()

        if root:
            queue.append(root)

        while len(queue) > 0:
            rightest_node = len(queue) - 1
            for i in range(len(queue)):
                root = queue.popleft()
                if root.left:
                    queue.append(root.left)
                if root.right:
                    queue.append(root.right)
                if i == rightest_node:
                    res.append(root.val)
        return res