# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def __eq__(self, node: Optional[TreeNode]) -> bool:
        if node is None:
            return False
        return self.val == node.val and self.left == node.left and self.right == node.right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None and q is None:
            return True

        # if (
        #     (p.left is None and q.left is not None)
        #     or (p.left is not None and q.left is None)
        #     or (p.right is None and q.right is not None)
        #     or (p.right is not None and q.right is None)
        #     or (p.left is not None and q.left is not None and p.left.val != q.left.val)
        #     or (p.right is not None and q.right is not None and p.right.val != q.right.val)  
        # ):
        #     return False
        if (
            (p is None and q is not None)
            or (p is not None and q is None)
            or (p.val != q.val)
            or (p.left != q.left or p.right != q.right)
        ):
            return False

        else:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)