# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []

        def get_height(node: Optional[TreeNode]):
            if not node: return -1
            
            left_height = get_height(node.left)
            right_height = get_height(node.right)
            current_height = max(left_height, right_height) + 1

            if len(res) == current_height:
                res.append([])

            res[current_height].append(node.val)
            return current_height
            

        get_height(root)
        return res