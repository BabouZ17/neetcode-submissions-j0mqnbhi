"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""
from collections import deque

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if not root: return list()

        res = list()
        def dfs(node: Optional['Node']):
            if not node: return

            for child in node.children:
                dfs(child)
            res.append(node.val)
        
        dfs(root)
        return res