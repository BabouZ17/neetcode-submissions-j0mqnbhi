
def is_valid(s: str) -> bool:
    return s.isalnum()

class Solution:

    def isPalindrome(self, s: str) -> bool:

        l, r = 0, len(s) - 1
        while l < r:
            while not is_valid(s[l].lower()) and l < r:
                l += 1
            while not is_valid(s[r].lower()) and l < r:
                r -= 1

            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True
            