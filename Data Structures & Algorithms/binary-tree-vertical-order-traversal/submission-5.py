# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque, defaultdict

class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        res = defaultdict(list)
        queue = deque([(root, 0)])
        minCol = maxCol = 0

        while queue:
            node, idx = queue.popleft()
            res[idx].append(node.val)
            minCol = min(minCol, idx)
            maxCol = max(maxCol, idx)

            if node.left:
                queue.append([node.left, idx - 1])
            if node.right:
                queue.append([node.right, idx + 1])
        return [res[i] for i in range(minCol, maxCol + 1)]


