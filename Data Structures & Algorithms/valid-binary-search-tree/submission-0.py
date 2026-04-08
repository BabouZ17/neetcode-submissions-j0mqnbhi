# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root.left is None and root.right is None:
            return True

        vals = []
        def dfs(root, vals):
            if root is None:
                return None
            dfs(root.left, vals)
            vals.append(root.val)
            dfs(root.right, vals)

        dfs(root,vals)

        prev = vals[0]
        for i in range(1, len(vals)):
            if vals[i] <= prev:
                return False
            prev = vals[i]
        return True