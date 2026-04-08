"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        curr_p, curr_q = p, q
        while curr_p != curr_q:
            curr_p = curr_p.parent if curr_p else q
            curr_q = curr_q.parent if curr_q else p
        return curr_p