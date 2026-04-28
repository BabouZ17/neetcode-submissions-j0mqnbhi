# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def dfs(node: Optional[TreeNode], currMax: int) -> int:
            if not node: return 0

            res = 1 if node.val >= currMax else 0
            newMax = max(currMax, node.val)

            res += dfs(node.left, newMax)
            res += dfs(node.right, newMax)
            return res

        return dfs(root, float("-inf"))
