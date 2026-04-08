from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        freqs_s = defaultdict(int)
        freqs_t = defaultdict(int)

        for i in range(len(s)):
            freqs_s[s[i]] += 1
            freqs_t[t[i]] += 1
        return freqs_s == freqs_t