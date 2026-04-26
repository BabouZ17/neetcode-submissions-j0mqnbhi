# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque, defaultdict
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return list()

        cols = defaultdict(list)
        queue = deque()
        queue.append([root, 0])
        max_col = min_col = 0

        while queue:
            for _ in range(len(queue)):
                node, column = queue.popleft()
                max_col = max(max_col, column)
                min_col = min(min_col, column)

                cols[column].append(node.val)
                if node.left:
                    queue.append([node.left, column - 1])
                if node.right:
                    queue.append([node.right, column + 1])
        return [cols[x] for x in range(min_col, max_col + 1)]
        

        