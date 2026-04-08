class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        first_word, second_word = {}, {}

        for i in range(len(s)):
            first_word[s[i]] = 1 + first_word.get(s[i], 0)
            second_word[t[i]] = 1 + second_word.get(t[i], 0)
        return first_word == second_word
