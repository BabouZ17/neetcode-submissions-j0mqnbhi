# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque, defaultdict

class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return list()

        cols = defaultdict(list)
        queue = deque([(root, 0)])
        while queue:
            node, pos = queue.popleft()
            if node is not None:
                cols[pos].append(node.val)
                queue.append((node.left, pos - 1))
                queue.append((node.right, pos + 1))
        return [cols[x] for x in sorted(cols)]