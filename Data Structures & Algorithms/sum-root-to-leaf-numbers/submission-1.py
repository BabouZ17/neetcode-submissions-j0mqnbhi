# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        total = 0
        def dfs(node: Optional[TreeNode], curr: list[int]):
            nonlocal total
            if node is None:
                return None

            curr.append(node.val)
            if node.left is None and node.right is None:
                total += int("".join([str(val) for val in curr]))
            dfs(node.left, curr[:])
            dfs(node.right, curr[:])

        dfs(root, [0])
        return total