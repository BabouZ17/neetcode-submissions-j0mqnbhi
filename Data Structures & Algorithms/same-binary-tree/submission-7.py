# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None and q is None:
            return True
        
        q1, q2 = deque([p]), deque([q])

        while q1 and q2:
            for _ in range(len(q1)):
                n1, n2 = q1.popleft(), q2.popleft()
                if n1 is None and n2 is None:
                    continue
                
                if n1 is None or n2 is None or n1.val != n2.val:
                    return False
                    
                q1.append(n1.left)
                q1.append(n1.right)
                q2.append(n2.left)
                q2.append(n2.right)
        return True