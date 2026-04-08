# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from typing import List

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(root: TreeNode, current_max: int):
            if root is None:
                return 0
            
            res = 1 if root.val >= current_max else 0
            current_max = max(current_max, root.val)

            res += dfs(root.left, current_max)
            res += dfs(root.right, current_max)
            return res   

        return dfs(root, root.val)
        