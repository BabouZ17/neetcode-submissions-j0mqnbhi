from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        letters = Counter(magazine)

        for letter in ransomNote:
            if letter in letters:
                letters[letter] -= 1
                if not letters[letter]:
                    del letters[letter]
            else:
                return False
        return True