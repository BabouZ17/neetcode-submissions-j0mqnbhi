from collections import Counter
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        freqs_t = Counter(t)

        for i in range(len(s)):
            freqs_t[s[i]] -= 1
        return list(freqs_t.elements())[0]
        