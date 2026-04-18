from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        letters = Counter(magazine)

        ransomLetters = list(ransomNote)
        while ransomLetters:
            char = ransomLetters.pop()
            if char in letters:
                letters[char] -= 1
                if letters[char] == 0:
                    del letters[char]
            else:
                return False
        return True