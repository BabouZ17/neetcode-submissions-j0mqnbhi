from collections import defaultdict

class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        letters = [0] * 26
        for word in words:
            for char in word:
                letters[ord(char) - ord('a')] += 1

        for letter in letters:
            if not letter:
                continue
            else:
                if letter % len(words) != 0: return False
        return True