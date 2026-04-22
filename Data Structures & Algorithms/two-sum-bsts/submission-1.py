# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def twoSumBSTs(self, root1: Optional[TreeNode], root2: Optional[TreeNode], target: int) -> bool:
        vals1, vals2 = [], []

        def dfs(node: Optional[TreeNode], vals: set[int]):
            if not node:
                return
            
            dfs(node.left, vals)
            vals.append(node.val)
            dfs(node.right, vals)
        
        dfs(root1, vals1)
        dfs(root2, vals2)

        i, j = 0, len(vals2) - 1
        while i < len(vals1) and 0 <= j:
            currSum = vals1[i] + vals2[j]
            if currSum == target:
                return True
            elif currSum < target:
                i += 1
            else:
                j -= 1
        return False