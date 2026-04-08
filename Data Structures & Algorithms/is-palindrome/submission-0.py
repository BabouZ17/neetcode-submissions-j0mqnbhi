import string

class Solution:
    def isPalindrome(self, s: str) -> bool:
        result = True

        for punctation in string.punctuation:
            s = s.replace(punctation, "")

        s = s.replace(" ", "").lower()

        i, j = 0, len(s) - 1

        for i in range(len(s)):
            if s[i] != s[j]:
                result = False
            i += 1
            j -= 1
        return result