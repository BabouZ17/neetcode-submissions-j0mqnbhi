# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:

        res = 0

        def dfs(node: Optional[TreeNode], low: int, high: int):
            nonlocal res

            if not node:
                return None
            
            if low <= node.val <= high:
                res += node.val

            dfs(node.left, low, high)
            dfs(node.right, low, high)

        dfs(root, low, high)
        return res 