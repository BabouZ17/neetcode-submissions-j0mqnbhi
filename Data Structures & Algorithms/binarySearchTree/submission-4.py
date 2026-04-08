from typing import List, Optional

class TreeNode:
    def __init__(self, key:int, val: int):
        self.key = key
        self.val = val
        self.left = self.right = None

class TreeMap:
    
    def __init__(self):
        self.root = None

    def insert(self, key: int, val: int) -> None:
        new_node = TreeNode(key, val)
        if self.root is None:
            self.root = new_node
            return
        
        current = self.root
        while True:
            if key < current.key:
                if current.left is None:
                    current.left = new_node
                    return
                current = current.left
            elif key > current.key:
                if current.right is None:
                    current.right = new_node
                    return
                current = current.right
            else:
                current.val = val
                return

    def get(self, key: int) -> int:
        current = self.root

        while current is not None:
            if key < current.key:
                if current.left is None:
                    break
                current = current.left
            elif key > current.key:
                if current.right is None:
                    break
                current = current.right
            else:
                return current.val
        return -1

    def findMin(self, node: TreeNode) -> int:
        while node and node.left:
            node = node.left
        return node

    def getMin(self) -> int:
        node = self.findMin(self.root)
        return node.val if node is not None else -1

    def getMax(self) -> int:
        curr = self.root
        while curr and curr.right:
            curr = curr.right
        return curr.val if curr is not None else -1

    def remove(self, key: int) -> None:
        self.root = self.removeHelper(self.root, key)

    def removeHelper(self, current: TreeNode, key: int) -> TreeNode:
        if current is None:
            return None

        if key > current.key:
            current.right = self.removeHelper(current.right, key)
        elif key < current.key:
            current.left = self.removeHelper(current.left, key)
        else:
            if current.left is None:
                return current.right
            elif current.right is None:
                return current.left
            else:
                min_node = self.findMin(current.right)
                current.key, current.val = min_node.key, min_node.val
                current.right = self.removeHelper(current.right, min_node.key)
        return current

    def getInorderKeys(self) -> List[int]:
        vals = []
        self.inorderTraversal(self.root, vals)
        return vals

    def inorderTraversal(self, root: TreeNode, vals: List[int]) -> None:
        if root is not None:
            self.inorderTraversal(root.left, vals)
            vals.append(root.key)
            self.inorderTraversal(root.right, vals)
