class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0:
            return True

        l, r = 0, 0

        while r < len(t):
            if l < len(s) and s[l] == t[r]:
                l += 1
            if l == len(s):
                return True
            r += 1
        return False