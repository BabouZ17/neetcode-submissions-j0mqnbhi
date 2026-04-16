"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:

        res = list()
        def dfs(node: Optional['Node']):
            if not node:
                return

            if node.children:
                for children in node.children:
                    dfs(children)
            res.append(node.val)
        
        dfs(root)
        return res
        