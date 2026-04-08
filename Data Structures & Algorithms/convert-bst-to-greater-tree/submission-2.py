# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        currSum = 0

        def dfs(node: Optional[TreeNode]):
            nonlocal currSum
            if node is None:
                return None
            
            dfs(node.right)
            tmp = node.val
            node.val += currSum
            currSum += tmp
            dfs(node.left)

        dfs(root)
        return root