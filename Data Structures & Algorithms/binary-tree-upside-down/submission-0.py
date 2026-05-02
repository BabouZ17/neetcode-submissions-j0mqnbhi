# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def upsideDownBinaryTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        curr = root
        prev = None
        prev_right = None

        while curr:
            next_node = curr.left
            right_node = curr.right

            curr.left = prev_right
            curr.right = prev

            prev = curr
            prev_right = right_node
            curr = next_node
        return prev