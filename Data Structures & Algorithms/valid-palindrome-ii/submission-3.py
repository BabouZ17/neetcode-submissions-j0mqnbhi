class Solution:
    def validPalindrome(self, s: str) -> bool:
        def is_palindrome(s: str, l: int, r: int) -> bool:
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        l, r = 0, len(s) - 1
        while l < r:
            if s[l] != s[r]:
                return is_palindrome(s, l+1, r) or is_palindrome(s, l, r-1)
            else:
                l += 1
                r -= 1
        return True