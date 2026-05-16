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

        while queue:
            for _ in range(len(queue)):
                node, idx = queue.popleft()
                res[idx].append(node.val)

                if node.left:
                    queue.append([node.left, idx - 1])
                if node.right:
                    queue.append([node.right, idx + 1])
        return [val[1] for val in sorted(res.items(), key=lambda x: x[0])]


