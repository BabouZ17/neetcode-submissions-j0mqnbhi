# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import heapq
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if root is None:
            return -1

        heap = list()
        def dfs(node: Optional[TreeNode]):
            if node is None:
                return None

            dfs(node.left)
            heap.append(node.val)
            dfs(node.right)
        
        dfs(root)
        while k - 1 > 0:
            heapq.heappop(heap)
            k -= 1
        return heapq.heappop(heap)