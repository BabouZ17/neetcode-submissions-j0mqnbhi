class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        n, m = len(word), len(abbr)
        i = j = 0

        while i < n and j < m:
            if abbr[j] == "0":
                return False
            
            if abbr[j] == word[i]:
                i, j = i + 1, j + 1
            elif abbr[j].isalpha():
                return False
            else:
                jump = 0
                while j < m and abbr[j].isdigit():
                    jump = 10 * jump + int(abbr[j])
                    j += 1
                i += jump
        return i == n and j == m
