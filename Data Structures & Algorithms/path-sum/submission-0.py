# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(node: Optional[TreeNode], target: int):
            if not node:
                return False

            if target - node.val == 0 and not node.left and not node.right:
                return True

            return dfs(node.left, target - node.val) or dfs(node.right, target - node.val)
        return dfs(root, targetSum)