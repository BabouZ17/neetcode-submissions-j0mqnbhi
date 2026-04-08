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
        res = list()
        
        def dfs(node: 'Node'):
            if node is None:
                return None
            
            for child in node.children:
                dfs(child)

            res.append(node.val)

        dfs(root)

        return res
