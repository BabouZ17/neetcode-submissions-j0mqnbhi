# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        max_path = 0


        def dfs(node: Optional[TreeNode], parent: Optional[TreeNode], length: int):
            nonlocal max_path
            if node is None: return

            length = length + 1 if parent is not None and node.val - parent.val == 1 else 1
            max_path = max(max_path, length)

            dfs(node.left, node, length)
            dfs(node.right, node, length)

        dfs(root, None, 1)
        return max_path