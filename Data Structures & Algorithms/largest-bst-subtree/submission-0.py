# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def largestBSTSubtree(self, root: Optional[TreeNode]) -> int:
        def dfs(node: Optional[TreeNode]) -> tuple[int, bool]:
            if not node: return (float("inf"), float("-inf"), 0)

            left_min, left_max, left_size = dfs(node.left)
            right_min, right_max, right_size = dfs(node.right)

            if left_max < node.val < right_min:
                curr_min = min(node.val, left_min)
                curr_max = max(node.val, right_max)
                curr_size = left_size + right_size + 1
                return (curr_min, curr_max, curr_size)
            else:
                return (float("-inf"), float("+inf"), max(left_size, right_size))
        return dfs(root)[2]


