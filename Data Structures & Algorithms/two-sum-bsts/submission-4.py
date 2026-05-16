# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def twoSumBSTs(self, root1: Optional[TreeNode], root2: Optional[TreeNode], target: int) -> bool:

        vals2 = set()
        def collect(node: Optional[TreeNode]):
            if not node: return

            vals2.add(node.val)
            collect(node.left)
            collect(node.right)

        collect(root2)

        def check(node: Optional[TreeNode]):
            if not node: return False

            if target - node.val in vals2:
                return True

            return check(node.left) or check(node.right)
        return check(root1)

