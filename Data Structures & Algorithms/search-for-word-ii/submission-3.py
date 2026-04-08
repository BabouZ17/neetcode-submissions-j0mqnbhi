class TrieNode:
    def __init__(self):
        self.children = dict()
        self.word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def add(self, word: str):
        curr = self.root
        for w in word:
            if w not in curr.children:
                curr.children[w] = TrieNode()
            curr = curr.children[w]
        curr.word = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        ROWS, COLS = len(board), len(board[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        res, visited = set(), set()
        trie = Trie()
        
        for word in words:
            trie.add(word)

        def dfs(r, c, node, word):
            if (
                min(r,c) < 0 or
                r == ROWS or
                c == COLS or
                (r, c) in visited or
                board[r][c] not in node.children
            ):
                return

            node = node.children[board[r][c]]
            word += board[r][c]
            visited.add((r, c))

            if node.word:
                res.add(word)

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                dfs(nr, nc, node, word)
            visited.remove((r, c))

        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, trie.root, "")

        return list(res)