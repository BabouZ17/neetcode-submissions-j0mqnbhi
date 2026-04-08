class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        res = float("-inf")

        l = 0
        for r in range(len(s)):
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
            res = max(res, r - l + 1)
            seen.add(s[r])
        return res if res != float("-inf") else 0