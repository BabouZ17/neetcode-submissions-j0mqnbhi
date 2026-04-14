class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        letters_map = dict()
        res = 0

        for i, char in enumerate(keyboard):
            letters_map[char] = i
        
        curr = 0
        for char in word:
            res += abs(letters_map[char] - curr)
            curr = letters_map[char]
        return res