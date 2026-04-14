class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        chars = [0] * 128
        for char in s:
            chars[ord(char)] += 1

        count = 0
        for c in chars:
            if c % 2:
                count += 1
        return count <= 1