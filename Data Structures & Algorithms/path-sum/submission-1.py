
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(node: Optional[TreeNode], target: int):
            if not node:
                return False

            target -= node.val
            if not node.left and not node.right:
                return target == 0

            return dfs(node.left, target) or dfs(node.right, target)
        return dfs(root, targetSum)