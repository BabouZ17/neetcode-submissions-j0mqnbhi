"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        clone = dict()

        def dfs(node: Optional['Node']):
            if node in clone:
                return clone[node]
            
            new_node = Node(val=node.val)
            clone[node] = new_node
            for neighbors in node.neighbors:
                new_node.neighbors.append(dfs(neighbors))
            return new_node

        return dfs(node) if node else None