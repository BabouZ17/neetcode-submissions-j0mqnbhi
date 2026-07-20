from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        letters = Counter(magazine)

        for letter in ransomNote:
            if not letters[letter]:
                return False
            else:
                letters[letter] -= 1
        return True