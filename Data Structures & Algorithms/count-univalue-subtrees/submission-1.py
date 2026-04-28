# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def countUnivalSubtrees(self, root: Optional[TreeNode]) -> int:
        if not root: return 0

        res = 0

        def dfs(node: Optional[TreeNode]):
            nonlocal res
            if not node: return True

            left_uni = dfs(node.left)
            right_uni = dfs(node.right)
            
            if not left_uni or not right_uni:
                return False
            
            if node.left and node.val != node.left.val:
                return False
            if node.right and node.val != node.right.val:
                return False

            res += 1
            return True

        dfs(root)
        return res