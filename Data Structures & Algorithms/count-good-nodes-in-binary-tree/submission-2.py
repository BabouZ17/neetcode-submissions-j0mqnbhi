# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node: Optional[TreeNode], prev_max: int):
            if node is None:
                return 0
            
            count = 0
            if node.val >= prev_max:
                count += 1
                prev_max = node.val
            
            count += dfs(node.left, prev_max)
            count += dfs(node.right, prev_max)
            return count
        
        count = 1
        count += dfs(root.left, root.val)
        count += dfs(root.right, root.val)
        return count