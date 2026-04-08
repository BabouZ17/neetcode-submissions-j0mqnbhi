class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        first_word_occurences = {}
        second_word_occurences = {}

        for char in s:
            first_word_occurences[char] = 1 + first_word_occurences.get(char, 0)
        
        for char in t:
            second_word_occurences[char] = 1 + second_word_occurences.get(char, 0)

        return first_word_occurences == second_word_occurences