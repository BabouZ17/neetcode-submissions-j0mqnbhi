from collections import Counter

class Solution:
    def firstUniqChar(self, s: str) -> int:
        freqs = Counter(s)

        for idx, char in enumerate(s):
            if freqs[char] == 1:
                return idx

        return -1