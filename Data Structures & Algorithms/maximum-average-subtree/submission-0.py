# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maximumAverageSubtree(self, root: Optional[TreeNode]) -> float:
        res = float("-inf")

        def dfs(node: Optional[TreeNode]) -> tuple[int, int]:
            nonlocal res
            if not node: return (0, 0) # sum, count

            left_sum, left_count = dfs(node.left)
            right_sum, right_count = dfs(node.right)

            total_sum = left_sum + right_sum + node.val
            total_count = left_count + right_count + 1

            res = max(res, total_sum / total_count)

            return (total_sum, total_count)

        dfs(root)
        return res
