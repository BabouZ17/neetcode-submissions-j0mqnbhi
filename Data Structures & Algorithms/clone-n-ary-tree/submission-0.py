"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children if children is not None else []
"""

from collections import deque

class Solution:
    def cloneTree(self, root: 'Node') -> 'Node':
        if not root: return None

        copy = Node(root.val, list())
        queue = deque([(root, copy)])

        while queue:
            for _ in range(len(queue)):
                original, node = queue.popleft()
                for child in original.children:
                    new_node = Node(child.val) if child else None
                    node.children.append(new_node)
                    queue.append((child, new_node))
        return copy
