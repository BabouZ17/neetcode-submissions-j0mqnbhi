class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length, l = 0, 0
        visited = set()

        for r in range(len(s)):
            while s[r] in visited:
                visited.remove(s[l])
                l += 1
            length = max(length, r - l + 1)
            visited.add(s[r])
        return length