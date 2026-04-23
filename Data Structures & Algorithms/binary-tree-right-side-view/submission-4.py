# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return list()

        queue = deque([root])
        res = list()
        while queue:
            last_node = queue[-1]
            for i in range(len(queue)):
                node = queue.popleft()
                if node == last_node:
                    res.append(node.val)
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
        return res
