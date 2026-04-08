# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        q1 = deque([p])
        q2 = deque([q])

        while q1 and q2:
            for _ in range(len(q1)):
                node_p = q1.popleft()
                node_q = q2.popleft()

                if node_p is None and node_q is None:
                    continue
                
                if node_p is None or node_q is None or node_p.val != node_q.val:
                    return False
                
                q1.append(node_p.left)
                q1.append(node_p.right)
                q2.append(node_q.left)
                q2.append(node_q.right)
        return True