class TrieNode:
    def __init__(self):
        self.children = {}
        self.endWord = False
    
class Trie:
    def __init__(self):
        self.root = TrieNode()

    def add(self, path: str):
        curr = self.root
        for c in path:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.endWord = True

    def search(self, path: str) -> bool:
        if not path:
            return True
            
        curr = self.root
        for c in path:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return curr.endWord

class FileSystem:

    def __init__(self):
        self.trie = Trie()
        self.paths = {}

    def createPath(self, path: str, value: int) -> bool:
        if path in self.paths:
            return False

        segments = path.split("/")
        parent = "/".join(segments[:-1])
        if not self.trie.search(parent):
            return False
        
        self.trie.add(path)
        self.paths[path] = value
        return True

    def get(self, path: str) -> int:
        if self.trie.search(path):
            return self.paths[path]
        return -1