class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        L, prev, res = 0, set(), 0

        for R in range(len(s)):
            while s[R] in prev:
                prev.remove(s[L])
                L += 1
            prev.add(s[R])
            res = max(res, R - L + 1)
        return res