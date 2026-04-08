from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_freqs = defaultdict(int)
        t_freqs = defaultdict(int)

        for i in range(len(s)):
            s_freqs[s[i]] += 1
            t_freqs[t[i]] += 1
        return s_freqs == t_freqs
        