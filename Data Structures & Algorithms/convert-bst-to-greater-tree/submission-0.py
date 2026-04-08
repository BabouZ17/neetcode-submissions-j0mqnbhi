# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None

        stack = list()
        def dfs(node: Optional[TreeNode]):
            if node is None:
                return None
            
            dfs(node.left)
            stack.append(node)
            dfs(node.right)

        dfs(root)
        prev = 0
        while stack:
            node = stack.pop()
            node.val += prev
            prev = node.val
        return root