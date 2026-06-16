from collections import Counter
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        count = Counter(t)
        for c in s:
            count[c] -= 1

        for c in count:
            if count[c] == 1:
                return c