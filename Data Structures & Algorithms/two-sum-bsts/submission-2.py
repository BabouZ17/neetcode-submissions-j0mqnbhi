class Solution:
    def twoSumBSTs(self, root1: Optional[TreeNode], root2: Optional[TreeNode], target: int) -> bool:
        
        def dfs(node: Optional[TreeNode], vals: list[int]):
            if not node: return

            dfs(node.left, vals)
            vals.append(node.val)
            dfs(node.right, vals)

        vals1, vals2 = [], []
        dfs(root1, vals1), dfs(root2, vals2)

        l, r = 0, len(vals2) - 1
        while l < len(vals1) and r >= 0:
            currSum = vals1[l] + vals2[r]
            if currSum == target:
                return True
            elif currSum > target: 
                r -= 1
            else: 
                l += 1

        return False