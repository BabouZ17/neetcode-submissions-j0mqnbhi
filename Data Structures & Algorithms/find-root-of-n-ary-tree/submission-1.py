"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def findRoot(self, tree: List['Node']) -> 'Node':
        value_sum = 0

        for t in tree:
            value_sum += t.val
            for child in t.children:
                value_sum -= child.val                    

        for t in tree:
            if t.val == value_sum:
                return t
