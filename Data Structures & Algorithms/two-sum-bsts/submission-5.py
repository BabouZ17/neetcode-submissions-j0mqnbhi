# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def twoSumBSTs(self, root1: Optional[TreeNode], root2: Optional[TreeNode], target: int) -> bool:
        def dfs(node: Optional[TreeNode], vals: set[int]):
            if not node: return

            vals.add(node.val)
            dfs(node.left, vals)
            dfs(node.right, vals)

        node_set1, node_set2 = set(), set()
        dfs(root1, node_set1)
        dfs(root2, node_set2)

        for value1 in node_set1:
            if target - value1 in node_set2:
                return True
        return False