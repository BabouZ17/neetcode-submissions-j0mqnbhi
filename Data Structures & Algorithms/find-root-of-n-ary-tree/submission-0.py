"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def findRoot(self, tree: List['Node']) -> 'Node':
        possible_root = set(node.val for node in tree)

        for t in tree:
            for child in t.children:
                if child.val in possible_root:
                    possible_root.remove(child.val)

        root_val = possible_root.pop()
        for t in tree:
            if t.val == root_val:
                return t
