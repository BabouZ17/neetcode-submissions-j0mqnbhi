class TreeNode:
    def __init__(self, key: int, val: int, left: TreeNode | None = None, right: TreeNode | None = None):
        self.key = key
        self.val = val
        self.left = left
        self.right = right

class TreeMap:
    
    def __init__(self):
        self.root = None

    def insert(self, key: int, val: int) -> None:
        new_node = TreeNode(key, val)
        if not self.root:
            self.root = new_node
            return
        
        current = self.root
        while 1:
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
        while current:
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

    def findMin(self, node: TreeNode):
        while node and node.left:
            node = node.left
        return node

    def getMin(self) -> int:
        node = self.findMin(self.root)
        return node.val if node else -1

    def getMax(self) -> int:
        current = self.root
        while current and current.right:
            current = current.right
        return current.val if current else -1

    def remove(self, key: int) -> None:
        self.root = self.removeHelper(key, self.root)

    def removeHelper(self, key: int, current: TreeNode | None) -> TreeNode:
        if not current:
            return None

        if key < current.key:
            current.left = self.removeHelper(key, current.left)
        elif key > current.key:
            current.right = self.removeHelper(key, current.right)
        else:
            if current.left is None:
                return current.right
            elif current.right is None:
                return current.left
            else:
                min_node = self.findMin(current.right)
                current.key, current.val = min_node.key, min_node.val
                current.right = self.removeHelper(min_node.key, current.right)
        return current

    def getInorderKeys(self) -> List[int]:
        keys = []
        self.inOrderTraversal(self.root, keys)
        return keys

    def inOrderTraversal(self, node: TreeNode, vals: list[int]) -> List[int]:
        if not node:
            return

        self.inOrderTraversal(node.left, vals)
        vals.append(node.key)
        self.inOrderTraversal(node.right, vals)
