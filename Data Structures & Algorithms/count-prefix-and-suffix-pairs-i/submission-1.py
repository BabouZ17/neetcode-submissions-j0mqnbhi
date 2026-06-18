class TrieNode:
    def __init__(self):
        self.children = {}
        self.count = 0

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def add(self, w: str):
        curr = self.root
        for c1, c2 in zip(w, reversed(w)):
            if (c1, c2) not in curr.children:
                curr.children[(c1, c2)] = TrieNode()
            curr = curr.children[(c1, c2)]
            curr.count += 1

    def count(self, w: str) -> int:
        curr = self.root
        for c1, c2 in zip(w, reversed(w)):
            if (c1, c2) not in curr.children:
                return 0
            curr = curr.children[(c1, c2)]
        return curr.count

class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        trie = Trie()
        res = 0

        for w in reversed(words):
            res += trie.count(w)
            trie.add(w)
        return res

